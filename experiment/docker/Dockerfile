# thanks to: https://github.com/uchida/docker-ubuntu-sshd

FROM ubuntu:16.04
# Description
LABEL maintainer="Ajay Tripathi <ajay39in@gmail.com>"
LABEL description="General purpose container"
LABEL base="ubuntu:16.04"
LABEL installed="OpenSSH, python3, nano"
# Install
RUN apt-get update \
    && apt-get install -y --no-install-recommends openssh-server python3 nano \
    && apt-get clean
# Configure
RUN mkdir /var/run/sshd \
    && sed -i 's|^PermitRootLogin .*|PermitRootLogin yes|' /etc/ssh/sshd_config \
    && sed -i 's|session\s*required\s*pam_loginuid.so|session optional pam_loginuid.so|g' /etc/pam.d/sshd
RUN echo 'root:root' | chpasswd
EXPOSE 80 443 22
CMD ["/usr/sbin/sshd", "-D"]
