FROM python

ENV FLASK_APP run.py

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN pip install gunicorn -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
