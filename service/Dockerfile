FROM python:3.8

RUN apt update && apt upgrade -y

COPY ./requirements.txt /root/service/requirements.txt
RUN pip install -r /root/service/requirements.txt

WORKDIR /root/service

CMD ["gunicorn", "-c", "gunicorn_conf.py", "wsgi:app"]
