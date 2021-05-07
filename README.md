# Notes Website

Test Website for playing around with, inspired by the
[Django Tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/).

Test code. Do not use in production.

## Instructions

Instructions for running on a VM

## Get files onto the machine
- Spin up VM with port 80 exposed
- Copy these files onto the VM
- Use python virtual-env to use python3 if needs be

## Set up nginx
- Install nginx: `sudo apt install nginx-core`
- Copy `nginx.conf` file to `/etc/nginx/conf.d/nginx.conf`
- Delete the competing file at: `/etc/nginx/sites-enabled/default`
- Reload nginx: `nginx -s reload`

## Set up Prometheus and Grafana
The nginx setup means that Prometheus and Grafana can be accessed via port 80 on paths
`/prometheus` and `/grafana` respectively.

To set Prometheus and Grafana up you need to do the following:
- Install Prometheus and Grafana onto the VM
- Run Prometheus behind proxy by following: https://www.robustperception.io/external-urls-and-path-prefixes
- Run Grafana behind proxy by following: https://grafana.com/tutorials/run-grafana-behind-a-proxy/
