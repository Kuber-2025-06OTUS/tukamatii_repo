## Для установки Локи
```
 helm upgrade --install -f kubernetes-logging/loki/loki-values.yml  loki grafana/loki -n logging --create-namespace 
```
## Для установки Графаны
```
helm upgrade --install -f kubernetes-logging/grafana/grafana-values.yml  grafana grafana/grafana -n grafana --create-namespace
```
## Для установки Промтейла
```
helm upgrade --install -f kubernetes-logging/promtail/promtail-vaules.yml promtail grafana/promtail -n promtail --create-namespace
```
