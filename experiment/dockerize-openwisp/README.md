# OPENWISP Dockerization Prototype

1. Tested installation of openwisp-controller & openwisp-network-topology modules and their requirements with a redis image.
2. Tested horizontal scaling with docker swarm & kubernetes.

### Idea:
I have created base images for openwisp-controller and openwisp-network-topology with all the system and python packages installed.
The user would be expected to use these base images and create images for their organization by following the usage instructions provided after setting the appropriate values for their organization in the `.env` file. 
Note: During this build, django settings like `SECRET_KEY` would be set in the image, hence the generated key is to kept in the private registry and the values of the `.env` can be saved privately for re-creating the images as well.


### Environment Variables:

For customization, you may change any of the following variables at run time using docker-compose file or build another image with the changed values using the dockerfile.

```
<var>=<default>
OPENWISP_CONTROLLER_IMAGE=atb00ker/ready-to-run:private-controller
OPENWISP_NETWORK_TOPOLOGY_IMAGE=atb00ker/ready-to-run:private-network-topology
DJANGO_REDIS_HOST=redis
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=<NO_VALUE>
```

### How to run:

Manipulate all the values in the `.env` file as you like, then run `make_secret_key.py` to generate a new secret key.
You can build the containers with `docker-compose up --build`. When the containers are ready, you should see OpenWISP Admin Interface on `127.0.0.1:8000/admin`. Default USER & PASS are `admin`.

Push these container in your private registry. (Keep the containers secure they contain the `SECRET_KEY`).
Pull the images in your production to deploy. :)