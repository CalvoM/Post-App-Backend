from flask import Blueprint,jsonify,request
from post_app_backend.models import Post,db
post_api = Blueprint('post_api',__name__)

@post_api.route('/get/posts/')
def get_all_posts():
    '''Get all posts'''
    posts = Post.query.all()
    posts_list = [p.serialize for p in posts]
    return jsonify(posts=posts_list)

@post_api.route('/add/posts/',methods=['POST'])
def add_post():
    post = request.json
    title = post['title']
    body = post['body']
    new_post = Post(title=title,body=body)
    db.session.add(new_post)
    db.session.commit()
    return {'resp':200}