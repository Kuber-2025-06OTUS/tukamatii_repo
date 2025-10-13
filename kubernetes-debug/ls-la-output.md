myapp:~# ps aux | grep -v grep | head -n 5
PID   USER     TIME  COMMAND
    1 root      0:00 nginx: master process nginx -g daemon off;
    7 33        0:00 nginx: worker process
    8 33        0:00 nginx: worker process
   62 root      0:00 bash
myapp:~# cd ^C
myapp:~# cd /proc/1/root
myapp:/proc/1/root# cd etc/nginx/
myapp:/proc/1/root/etc/nginx# ls
conf.d           dhparam4096.pem  koi-utf          mime.types       nginx.conf       site.conf.d      uwsgi_params
dhparam2048.pem  fastcgi_params   koi-win          modules          scgi_params      sites.d          win-utf
