# OPENWISP Dockerization Prototype

1. Tested installation of openwisp-controller, openwisp-users, openwisp-utils modules and their requirements with a redis image.
2. Tested horizontal scaling with docker swarm & kubernetes.

### Environment Variables:

For customization, you may change any of the following variables at run time using docker-compose file or build another image with the changed values using the dockerfile.

```
<var>=<default>
DJANGO_REDIS_HOST=redis
DJANGO_DEBUG=False
```

### How to run:

You can run the containers with `docker-compose up`. When the containers are ready, you should see OpenWISP Admin Interface on `127.0.0.1:8000/admin`. Default USER & PASS are `admin`.