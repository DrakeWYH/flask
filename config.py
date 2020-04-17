import os

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'huaweiserver'
USERNAME = 'root'
PASSWORD = 'admin123'
DB_URI = 'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}?charset=utf8'.format(username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT, database=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CSRF_ENABLED = True
# SECRET_KEY = os.urandom(24)
SECRET_KEY = '123123123'
# DEBUG = True
