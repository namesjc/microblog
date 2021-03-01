FROM python

ENV FLASK_APP run.py

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]