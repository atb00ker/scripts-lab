FROM atb00ker/test:ubuntu16.04
# Description
LABEL maintainer="Ajay Tripathi <ajay39in@gmail.com>"
LABEL description="OpenWISP"
LABEL base="atb00ker/test:ubuntu16.04"
# Install
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python-software-properties \
    software-properties-common \
    rsyslog systemd systemd-cron curl \
    && apt-get clean
# Configure
EXPOSE 80 443 22
CMD ["/usr/sbin/sshd", "-D"]
