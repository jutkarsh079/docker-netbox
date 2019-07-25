docker-netbox
====================

Docker compose file for running netbox


Contents
-------------



Instruction building image
-------------
No special instructions.

```

```

Instruction running docker-compose.yml
-------------

The repository is compatible with the puppet naturalis/puppet-docker_compose manifest and can be deployed using that manifests. 

#### preparation
- Copy env.template to .env and adjust variables. 


````
docker-compose up -d
````

Usage
-------------



If there is a valid traefik.toml with or without SSL then both services can be accessed through port 80/443. 
It is advised to setup firewall rules and only allow 80/443 to the server running the docker-compose project, use port 8080,9000 and 8081 using a SSH tunnel.


