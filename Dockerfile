FROM python:3.9.2-slim-buster

ENV FLASK_APP run.py

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

ENV PROMETHEUS_MULTIPROC_DIR /tmp
ENV prometheus_multiproc_dir /tmp

RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
