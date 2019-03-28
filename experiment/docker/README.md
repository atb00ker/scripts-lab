# OPENWISP Dockerization Prototype

1. Tested installation of openwisp-controller, openwisp-users, openwisp-utils modules and their requirements with a redis image.
2. Tested horizontal scaling with docker swarm & kubernetes.

### Environment Variables:
These environement variables must be set before using docker-compose.

```
<var>=<default>
DOCKER_IMAGE=atb00ker/ready-to-run:openwisp-web
DJANGO_REDIS_HOST=localhost
DJANGO_DEBUG=True
```
You can simply edit the `.env` file to achieve this.

Note: (For pipenv users) `.env` is a special file in pipenv as well 
so, simply changing this file wouldn't work. You'll need to set these variables
in environement variables of your terminal terminal.
You can simply write a file with environement variables and use a command like 
`export $(cat config/kubes.env | xargs)` to change the values.

You can run the containers with `docker-compose up`. When the containers are ready, you should see OpenWISP Admin Interface on `127.0.0.1:8000/admin`. Default USER & PASS are `admin`.