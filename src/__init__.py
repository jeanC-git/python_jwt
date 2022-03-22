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


@app.errorhandler(500)
def error500(e):
    return {
        'msg': e.description if e.description else 'Server error.'
    }


@app.errorhandler(401)
def error401(e):
    return {
        'msg': e.description if e.description else 'Unauthorized.'
    }


@app.errorhandler(403)
def error403(e):
    return {
        'msg': e.description if e.description else 'Forbidden.'
    }
