from flask import Blueprint,json
from post_app_backend.models import Post,db
post_api = Blueprint('post_api',__name__)

@post_api.route('/get/posts')
def get_all_posts():
    '''Get all posts'''
    posts = Post.query.all()
    posts_list = [p.deserialise for p in posts]
    return jsonify(posts=posts_list)