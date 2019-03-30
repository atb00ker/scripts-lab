FROM atb00ker/ready-to-run:base-controller

COPY ./data/ /opt/openwisp/

ENV DJANGO_REDIS_HOST redis
ENV DJANGO_DEBUG False

RUN chmod +x /opt/openwisp/init_command.sh

EXPOSE 8000

CMD /opt/openwisp/init_command.sh