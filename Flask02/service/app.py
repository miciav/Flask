from flask import Flask
from flask_migrate import Migrate
from models import db
from views import service_blueprint


def create_app(config_filename):
    application = Flask(__name__)
    # configuring the Flask application
    application.config.from_object(config_filename)
    db.init_app(application)
    application.register_blueprint(service_blueprint, url_prefix='/service')
    migrate = Migrate(application, db)
    return application


if __name__ == "__main__":
    app = create_app('config')
    app.run()

