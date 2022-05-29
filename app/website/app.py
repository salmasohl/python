from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from .views import views
from app.website.routes.auth import auth
db = SQLAlchemy()
migrate = Migrate()

# import all models to work with migrations
# migrate after any model change in terminal using : flask db migrate | flask db upgrade
# see https://flask-migrate.readthedocs.io/en/latest/
from app.website import models

def create_app():
    app = Flask(__name__)
    # change the connection string to match 'mysql://username:password@host/database'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/connectivity-monitor'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
