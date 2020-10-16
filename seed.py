from models import User,db,Post
from app import app

#create all tables

db.create_all()


User.query.delete()

#add user
taylor=User(first_name='taylor',last_name='swift',image_url='https://lh3.googleusercontent.com/uJ1hiKnfxQTtodPzshcUpb7S8IAKfsb5yyj4md_6wTiycwuG58Ptb41wJeARRkDYoMex4eyV2UETVPNqzOH7RRL2')
trump = User(first_name='trump',last_name='trump',image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRpcSfEtU0KJnSC9X5Eq6zR3hDODoS4Oeso4Q&usqp=CAU')
katty = User(first_name='katty',last_name='perry',image_url='https://www.iwmbuzz.com/wp-content/uploads/2020/10/best-of-katy-perrys-songs-that-have-the-highest-views-2-920x518.jpg')

#add user
db.session.add(taylor)
db.session.add(trump)
db.session.add(katty)

#commit
db.session.commit()

Post.query.delete()

taylor_post=Post(title="vote",content="I spoke to @vmagazine about why I’ll be voting for Joe Biden for president.",user_id=1)
trump_post=Post(title="JoeBiden",content="Joe Biden is a PUPPET of CASTRO-CHAVISTAS",user_id=2)
trump_posttwo=Post(title="Whitner",content="Governor Whitmer of Michigan has done a terrible job. ",user_id=2)
katty_post=Post(title="smile",content="IT’S HERE! IT’S REALLY HERE! (sent from my hospital bed lol)",user_id=3)

db.session.add(taylor_post)
db.session.add(trump_posttwo)
db.session.add(trump_post)
db.session.add(katty_post)

db.session.commit()

Tag.query.delete()

tag_one = Tag(id=1,name="smile everyday")
tag_two = Tag(id=2,name="BLM")
tag_three=Tag(id=3,name="rainbow")

db.session.add_all([tag_one,tag_two,tag_three])
db.session.commit()



