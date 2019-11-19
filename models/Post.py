from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from post_app_backend import post_app
post_app.config['SQLALCHEMY_DATABASE_URI']='postgresql://d1r3ct0r:SaminSky!@localhost/d1r3ct0r'
db = SQLAlchemy(post_app) #yet to add flask app

class Post(db.Model):
    __tablename__="Post"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(40), nullable = False)
    body = db.Column(db.Text, nullable = False)
    posted_at = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    upvotes = db.Column(db.Integer,nullable=False,default=0)
    downvotes = db.Column(db.Integer,nullable=False,default=0)

    def __rep__(self):
        return "<Post %r>"%self.title

    @property
    def serialize(self):
        return{
            'title':self.title,
            'body':self.body,
            'posted_at':self.posted_at,
            'upvotes':self.upvotes,
            'downvotes':self.downvotes
        }

db.create_all()
