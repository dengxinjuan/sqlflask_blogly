"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db,User,Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    return redirect("/users")

@app.route("/users")
def list_users():
    """list all users """
    users = User.query.all()
    return render_template("users.html",users=users)

@app.route("/users/new", methods=["GET"])
def show_form():
    """show add user form"""
    return render_template("form.html")

@app.route("/users/new", methods=["POST"])
def add_user():
    """add user"""
    firstname= request.form['first_name']
    lastname=request.form['last_name']
    imageurl = request.form['image_url']
    imageurl=imageurl if imageurl else None

    newuser = User(first_name = firstname, last_name=lastname,image_url=imageurl)
    db.session.add(newuser)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:id>", methods=["GET"])
def show_addform(id):
    """show user details and edit button"""
    user = User.query.get_or_404(id)
    return render_template("detail.html",user=user)

@app.route("/users/<int:id>/edit",methods=["GET"])
def show_editform(id):
    """show edit form"""
    return render_template("editform.html")


@app.route("/users/<int:id>/edit",methods=["POST"])
def process_editform(id):
    """show edit form"""
    edituser= User.query.get_or_404(id)
    edituser.first_name= request.form['first_name']
    edituser.last_name=request.form['last_name']
    edituser.image_url = request.form['image_url']
    db.session.add(edituser)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:id>/delete")
def delete(id):
    """show edit form"""
    deleteuser = User.query.get_or_404(id)
    db.session.delete(deleteuser)
    db.session.commit()
    return render_template("delete.html",user=deleteuser)


@app.route("/users/<int:id>/posts/new", methods=["GET"])
def add_post(id):
    """show form for that user"""
    user = User.query.get_or_404(id)
    return render_template("addpost.html",user=user)

@app.route("/users/<int:id>/posts/new", methods=["POST"])
def process_add(id):
    """ add a post for that user"""
    user = User.query.get_or_404(id)
    title = request.form["title"]
    content= request.form["content"]
    newpost= Post(title=title,content=content,user_id=id)
    db.session.add(newpost)
    db.session.commit()

    return redirect(f"/users/{id}")

@app.route("/posts/<int:postid>",methods=["GET"])
def show_post(postid):
    """show a specific post by postid"""
    post = Post.query.get_or_404(postid)
    return render_template("post.html",post=post)

@app.route("/posts/<int:postid>/delete")
def delete_post(postid):
    """ delete a post"""
    deletepost = Post.query.get_or_404(postid)
    db.session.delete(deletepost)
    db.session.commit()

    return render_template("deletepost.html",deletepost=deletepost)

#todo: GET /posts/[post-id]/edit
#Show form to edit a post, and to cancel (back to user page).


#POST /posts/[post-id]/edit
#Handle editing of a post. Redirect back to the post view.


