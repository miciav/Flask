import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
# Replace your_user_name with the user name you configured for the database
# Replace your_password with the password you specified for the database user
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}".format(
    DB_USER="your_user_name", DB_PASS="your_password", DB_ADDR="localhost", DB_NAME="flask_notifications",
    DB_PORT="55000")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
