FROM python:3.9.2-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

COPY app app
COPY run.py config.py gunicorn_config.py worker.py boot.sh ./
RUN chmod +x boot.sh

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

ENV FLASK_APP run.py
ENV PROMETHEUS_MULTIPROC_DIR /tmp
ENV prometheus_multiproc_dir /tmp

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
