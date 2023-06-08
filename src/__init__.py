from flask import Flask, g
import os
from src.routes.task import task_blueprint
from . import db

def create_app():
    app = Flask(__name__,
                instance_relative_config=True)
    
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
        SECRET_KEY= os.environ.get("SECRET_KEY"),
    )

    app.register_blueprint(task_blueprint)

    db.init_app(app)


    return app

