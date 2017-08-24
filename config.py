import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED=True
SECRET_KEY='very-long-string-here'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
