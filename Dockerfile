FROM python:3.9

RUN apt update -y && apt upgrade -y && apt install -y mpc vim
RUN mkdir /root/app \
  && touch /var/run/gunicorn.pid \
  && pip install gunicorn Flask

COPY . /root/app/

RUN chmod +x /root/app/run

WORKDIR /root/app
  
EXPOSE 7170

CMD ["/bin/sh", "run"]

