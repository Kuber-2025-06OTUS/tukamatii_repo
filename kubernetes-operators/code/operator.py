import kopf
import kubernetes.client
from kubernetes.client.rest import ApiException
import yaml

@kopf.on.create('otus.homework', 'v1', 'mysqls')
def create_fn(spec, logger, **kwargs):
    name = kwargs["body"]["metadata"]["name"]
    namespace = kwargs["body"]["metadata"]["namespace"]
    
    print("Name is %s\n" % name)
    # Create the deployment spec
    deployment = yaml.safe_load(f"""
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: {name}-deployment
        spec:
          selector:
            matchLabels:
              app: {name}
          strategy:
            type: Recreate
          template:
            metadata:
              labels:
                app: {name}
            spec:
              containers:
                - image:  {spec.get('image')}
                  name: mysql
                  env:
                    - name: MYSQL_ROOT_PASSWORD
                      value: {spec.get('password')}
                    - name: MYSQL_DATABASE
                      value: {spec.get('database')}
                  ports:
                    - containerPort: 3306
                      name: mysql
                  volumeMounts:
                    - mountPath: /data
                      name: data-dir
              volumes:
                - name: data-dir
                  persistentVolumeClaim:
                    claimName: {name}-pvc

    """)

    service = yaml.safe_load(f"""

        apiVersion: v1
        kind: Service
        metadata:
          name: {name}-service
        spec:
          selector:
                app: {name}
          ports:
            - protocol: TCP
              port: 3306
              targetPort: mysql
          type: ClusterIP

    """)
    pv = yaml.safe_load(f"""
        apiVersion: v1
        kind: PersistentVolume
        metadata:
          name: {name}-pv
        spec:
          capacity:
            storage: 1Gi
          storageClassName: "mynewclass"
          claimRef:
            name: {name}-pvc
          accessModes:
            - ReadWriteOnce
          hostPath:
            path: "/mnt/data"
    """)

    pvc = yaml.safe_load(f"""
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          name: {name}-pvc
        spec:
          storageClassName: "mynewclass"
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: {spec.get('storage_size')}
    """)


    # Make it our child: assign the namespace, name, labels, owner references, etc.
    kopf.adopt(pv)
    kopf.adopt(pvc)
    kopf.adopt(deployment)
    kopf.adopt(service)

    # Actually create an object by requesting the Kubernetes API.
    api = kubernetes.client.AppsV1Api()
    try:
        depl = api.create_namespaced_deployment(namespace, deployment)
        logger.info(f"Deployment redis-{name} created")
    except ApiException as e:
        logger.error(f"Failed to create Deployment: {e}")
        raise

    api = kubernetes.client.CoreV1Api()
    try:
        svc = api.create_namespaced_service( namespace, service)
        logger.info(f"Service redis-{name} created")
    except ApiException as e:
        logger.error(f"Failed to create Service: {e}")
        raise
    
    api = kubernetes.client.CoreV1Api()
    try:
        pvc = api.create_namespaced_persistent_volume_claim( namespace, pvc)
        logger.info(f"Service redis-{name} created")
    except ApiException as e:
        logger.error(f"Failed to create Service: {e}")
        raise

    api = kubernetes.client.CoreV1Api()
    try:
        pvc = api.create_persistent_volume( namespace, pv)
        logger.info(f"Service redis-{name} created")
    except ApiException as e:
        logger.error(f"Failed to create Service: {e}")
        raise
    

@kopf.on.delete('otus.homework', 'v1', 'mysqls')
def delete_fn(logger, **kwargs):
    name = kwargs["body"]["metadata"]["name"]
    namespace = kwargs["body"]["metadata"]["namespace"]

    # Удаляем Deployment
    api = kubernetes.client.AppsV1Api()
    try:
        api.delete_namespaced_deployment(f'{name}-deployment', namespace)
        logger.info(f"Deployment redis-{name} deleted")
    except ApiException as e:
        if e.status != 404:
            logger.error(f"Failed to delete Deployment: {e}")


    # Удаляем Service
    api = kubernetes.client.CoreV1Api()
    try:
        api.delete_namespaced_service(f'{name}-service', namespace)
        logger.info(f"Service redis-{name} deleted")
    except ApiException as e:
        if e.status != 404:
            logger.error(f"Failed to delete Service: {e}")

    api = kubernetes.client.CoreV1Api()
    try:
        api.delete_persistent_volume(f'{name}-pv')
        logger.info(f"PV {name}-pv deleted")
    except ApiException as e:
        if e.status != 404:
            logger.error(f"Failed to delete pv: {e}")

    api = kubernetes.client.CoreV1Api()
    try:
        api.delete_namespaced_persistent_volume_claim(f'{name}-pvc', namespace)
        logger.info(f"PVC {name}-pvc deleted")
    except ApiException as e:
        if e.status != 404:
            logger.error(f"Failed to delete pvc: {e}")