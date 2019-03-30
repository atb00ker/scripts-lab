FROM atb00ker/ready-to-run:base-network-topology

COPY  ./data/ /opt/openwisp/

ENV DJANGO_DEBUG False

RUN chmod +x /opt/openwisp/init_command.sh

EXPOSE 8001

CMD /opt/openwisp/init_command.sh