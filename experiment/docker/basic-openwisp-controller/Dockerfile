FROM atb00ker/sshable:ubuntu18


# Install dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    sudo curl cron git \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Install Ansible via pip.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential libffi-dev libssl-dev python3-pip python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

RUN pip3 install --upgrade setuptools \
    && pip3 install ansible

RUN ansible-galaxy install openwisp.openwisp2
COPY playbook.yml . 
COPY hosts .
