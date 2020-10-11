
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


"""Models for Blogly."""
class User(db.Model):
    
    """define the basic user model"""
    __tablename__ = 'blog_user'

    id = db.Column(db.Integer,
    primary_key=True,
    autoincrement=True)

    first_name = db.Column(db.Text,
    nullable=False)

    last_name = db.Column(db.Text,
    nullable=False)

    image_url =db.Column(db.Text,
    nullable=False,
    default="https://www.clker.com/cliparts/d/L/P/X/z/i/no-image-icon-hi.png")

    posts = db.relationship("Post", backref="user",cascade="all, delete-orphan")

    def get_full_name(self):
        """Get full name for user"""
        return f"{self.first_name} {self.last_name}"


"""Model for Post"""

class Post(db.Model):
    """define the basic post model"""
    __tablename__ = "posts"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title= db.Column(db.Text,nullable=False)
    content = db.Column(db.Text,nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id'),nullable=False)
    
    def friendly_date(self):
        """Return nicely-formatted date."""
        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")
