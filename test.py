import unittest
from flask.ext.testing import TestCase
from flask.ext.login import current_user
from project import app, db
from project.models import User, BlogPost

class BaseTestCase(TestCase):
    """A base test case """
    
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app
        
    def setUp(self):
        db.create_all()
        db.session.add(BlogPost("Test post", "This is a test. Only a test"))
        db.session.add(User("admin", "admin@example.com", "admin"))
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        

class FlaskTestCase(BaseTestCase):
    
    #Ensure that flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
      

    # ensure the main page requires a login
    def test_main_route_requires_login(self):
       response = self.client.get('/', follow_redirects=True)
       self.assertTrue(b'Please log in to access this page.' in response.data) 
   
    # ensure the posts show on the main page
    def test_posts_list(self):
        response = self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'Test post', response.data)  
      
  
 
class UsersViewTests(BaseTestCase):
    
    # ensure the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Please Login' in response.data)
   
   
    # ensure the login behaves correctly with the correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            self.assertIn(b'You are now logged in!', response.data) 
            self.assertTrue(current_user.name=='admin')
            self.assertTrue(current_user.is_active())
        
        
    # ensure the login behaves correctly with the wrong credentials
    def test_incorrect_login(self):
        response = self.client.post('/login', data=dict(username="test", password="admin"), follow_redirects=True)
        self.assertIn(b'Invalid credentials. Please try again.', response.data) 
        
    # ensure the logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You are now logged out!', response.data) 
            self.assertFalse(current_user.is_active())
    
    # ensure the logout page requires a login
    def test_logout_route_requires_login(self):
       response = self.client.get('/logout', follow_redirects=True)
       self.assertTrue(b'Please log in to access this page.' in response.data)          
    
    # ensure a user can register
    def test_user_registration(self):
        with self.client:
            response = self.client.post('/register', data=dict(username="Michael", email="michael@example.com", password="michael", confirm="michael"), follow_redirects=True)
            self.assertIn(b'Welcome to the BucketList Application', response.data) 
            self.assertTrue(current_user.name=='Michael')
            self.assertTrue(current_user.is_active())
       
        
if __name__ == '__main__':
    unittest.main()