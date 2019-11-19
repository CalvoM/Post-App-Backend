from flask import Flask

post_app = Flask(__name__)

from .models import Post,db
