WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
DEBUG = True


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = ''
MYSQL_DATABASE_DB = 'flask_game'
MYSQL_DATABASE_HOST = 'localhost'