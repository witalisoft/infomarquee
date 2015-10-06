FROM ubuntu:14.04
MAINTAINER Witold Duranek <contact@witalis.net>
RUN apt-get update && apt-get -y install python-redis \
    redis-server \
    gunicorn \
    supervisor \
    python-pip
RUN pip install flask
RUN mkdir -p /opt/infomarquee
ADD app /opt/infomarquee    
ADD supervisor/supervisord.conf /etc/supervisor/
ADD supervisor/conf.d/gunicorn.conf /etc/supervisor/conf.d/
ADD supervisor/conf.d/redis.conf /etc/supervisor/conf.d/
EXPOSE 8000
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n" ]
