from models import User,db
from app import app

#create all tables
db.drop_all()
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


