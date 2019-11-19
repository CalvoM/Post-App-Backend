from flask import Flask

post_app = Flask(__name__)

from .models import Post,db
from .apis import post_api
post_app.register_blueprint(post_api)
@post_app.route('/')
def home():
    return "Am home"
