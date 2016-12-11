from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
    
    #Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
      
    # ensure the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please Login' in response.data)
   
   
    # ensure the login behaves correctly with the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'You are now logged in!', response.data) 
        
        
    # ensure the login behaves correctly with the wrong credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="test", password="admin"), follow_redirects=True)
        self.assertIn(b'Invalid credentials. Please try again.', response.data) 
        
    # ensure the logout behaves correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You are now logged out!', response.data) 
   
    # ensure the main page requires a login
    def test_main_route_requires_login(self):
       tester = app.test_client(self)
       response = tester.get('/', follow_redirects=True)
       self.assertTrue(b'You need to login first' in response.data) 
   
    # ensure the logout page requires a login
    def test_logout_route_requires_login(self):
       tester = app.test_client(self)
       response = tester.get('/logout', follow_redirects=True)
       self.assertTrue(b'You need to login first' in response.data)  
   
    # ensure the posts show on the main page
    def test_posts_list(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'Shell Test', response.data)  
      
   
        
if __name__ == '__main__':
    unittest.main()