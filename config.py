import os
# from dotenv import load_dotenv

# load_dotenv('.env')

basedir = os.path.abspath(os.path.dirname(__file__))
database_url = os.environ.get('DATABASE_URL')
database_password = os.environ.get('DATABASE_PASSWORD')
redis_url = os.environ.get('REDIS_URL') 
elasticsearch_url = os.environ.get('ELASTICSEARCH_URL')

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{database_password}@{database_url}:3306/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'Cerulean'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    ADMINS = ['adiachan@foxmail.com']
    POSTS_PER_PAGE = 3
    ELASTICSEARCH_URL = 'http://{elasticsearch_url}:9200'
    REDIS_URL = f'redis://{redis_url}:6379/0' or 'redis://'
