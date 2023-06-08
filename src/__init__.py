from flask import Flask, g
import os
from src.routes.task import task_blueprint
from src.routes.auth import auth_blueprint
from . import db
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__,
                instance_relative_config=True)
    
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
        SECRET_KEY= os.environ.get("SECRET_KEY"),
        JWT_SECRET_KEY= os.environ.get("JWT_SECRET_KEY")
    )

    JWTManager(app)

    app.register_blueprint(task_blueprint)
    app.register_blueprint(auth_blueprint)

    db.init_app(app)


    return app

