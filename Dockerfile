FROM fedora:30

ENV LANG=en_US.UTF-8 \
    ANSIBLE_STDOUT_CALLBACK=debug \
    USER=sentinel-downloader \
    HOME=/home/sentinel-downloader \
    WORKDIR=/src

RUN dnf install -y ansible

RUN mkdir /data

VOLUME /data

COPY files/install-deps.yaml /src/files/

# Install dependencies. If you want to add any please do so in files/install-deps.yaml
RUN cd /src/ \
    && ansible-playbook -vv -c local -i localhost, files/install-deps.yaml \
    && dnf clean all

COPY ./ ${WORKDIR}/

# setuptools-scm
COPY .git /src/.git
COPY sentinel_downloader/ /src/sentinel_downloader/

RUN pip3 install ${WORKDIR}/ \
    && rm -rf ~/.cache/*
