# rp4
small flask app to expose temp/humitdy data as metrics from a raspberry pi dht11 sensor. 

Metrics scraped by prometheus and fed into some Grafana dashboards available to display historical data from the pi

docker build -t anasypany/dht11-server:0.1 .
