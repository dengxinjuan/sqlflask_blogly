from unittest import TestCase

from app import app
from models import db,User,Post

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """test model for User"""

    def setup(self):
        """clean up all existing user"""
        User.query.delete()

    def tearDown(self):
        """clean up any fouled transcation"""
        db.session.rollback()
    
    def test_getfullname(self):
        """test get full name function"""
        user=User(first_name="xinjuan",last_name="deng",image_url=None)
        self.assertEquals(user.get_full_name(),"xinjuandeng")

    def test_userhome(self):
        with app.test_client() as client:
            """test user name in home page"""
            user=User(first_name="xinjuan",last_name="deng",image_url=None)
            db.session.add(user)
            db.session.commit()

            resp = client.get("/users")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code,200)
            self.assertIn("xinjuandeng",html)




