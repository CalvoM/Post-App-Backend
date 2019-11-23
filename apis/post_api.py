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

@post_api.route('/increment_upvote/',methods=['POST'])
def increment_post_vote():
    post = request.json
    print(post)
    id = post['id']
    increment_value = post['increment_value']
    post_to_update = Post.query.filter_by(id=post['id']).first()
    post_to_update.upvotes +=1
    db.session.commit()
    print(post_to_update)
    return {'resp':200}

@post_api.route('/increment_downvote/',methods=['POST'])
def decrement_post_vote():
    post = request.json
    print(post)
    id = post['id']
    increment_value = post['increment_value']
    post_to_update = Post.query.filter_by(id=post['id']).first()
    post_to_update.downvotes +=1
    db.session.commit()
    print(post_to_update)
    return {'resp':200}
