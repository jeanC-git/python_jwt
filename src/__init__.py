from flask import Flask
from src.models.User import User
from src.databases.db import db

from src.routes import auth_routes

app = Flask(__name__)
app.config.from_object("config.DebugConfig")
db.init_app(app)

app.register_blueprint(auth_routes.auth)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
