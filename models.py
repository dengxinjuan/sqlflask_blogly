
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


"""Models for Blogly."""
class User(db.Model):
    
    """define the basic user model"""
    __tablename__ = 'user'

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










