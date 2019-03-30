FROM python:3.7-alpine

WORKDIR /opt/openwisp

RUN apk add --update --no-cache build-base libffi-dev openssl-dev python3-dev zlib-dev jpeg-dev sqlite bash --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing gdal-dev libspatialite-dev geos-dev
RUN wget http://download.osgeo.org/geos/geos-3.7.1.tar.bz2 && tar xjf geos-3.7.1.tar.bz2 && cd geos-3.7.1/ && ./configure && make && make install && rm -rf /opt/openwisp/geos-3.7.1.tar.bz2 /opt/openwisp/geos-3.7.1  

COPY ./requirements.txt /opt/openwisp/requirements.txt
RUN pip install -r requirements.txt