# tests/test_users.py


import unittest

from flask import request
from flask.ext.login import current_user
from base import BaseTestCase
from project import bcrypt
from project.models import User



class TestUser(BaseTestCase):
    
    # ensure the user can register
    def test_user_registration(self):
        with self.client:
            response = self.client.post('/register', data=dict(username="Michael", email="michael@example.com", password="michael", confirm="michael"), follow_redirects=True)
            self.assertIn(b'Current BucketList Items', response.data) 
            self.assertTrue(current_user.name=='Michael')
            self.assertTrue(current_user.is_active())
            user = User.query.filter_by(email='michael@example.com').first()
            self.assertTrue(str(user) == '<name - Michael>')
            

    def test_get_by_id(self):
        
        # ensure the id is correct for the current/logged in user
        with self.client:
            self.client.post('/login', data=dict(username="admin", password='admin'), follow_redirects=True)
            self.assertTrue(current_user.id == 1)
            self.assertFalse(current_user.id == 20)
            
    
    def test_check_password(self):
        
        # ensure given password is correct after unhashing
        user = User.query.filter_by(email='admin@example.com').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'admin'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))
        
        
    # ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registration(self):
        with self.client:
            response = self.client.post('/register', data=dict(username='Michael',email='michaeil', password='python', confirm='python'), follow_redirects=True)
            self.assertIn(b'Invalid email address.', response.data)
            self.assertIn(b'/register', request.url)
    
    
    
    

class UserViewsTests(BaseTestCase):

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertIn(b'Please sign in', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post('/login', data=dict(username="admin", password="admin"),follow_redirects=True)
            self.assertIn(b'You are now logged in!', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active())

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.client.post('/login', data=dict(username="wrong", password="wrong"),follow_redirects=True        )
        self.assertIn(b'Invalid credentials. Please try again.', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You are now logged out!', response.data)
            self.assertFalse(current_user.is_active())

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
        
    # Ensure that add item page requires user login
    def test_additem_route_requires_login(self):
        response = self.client.get('/addItem', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
        
    # Ensure that pagination shows up after login
    def test_pagination_shows(self):
        with self.client:
            response = self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            self.assertIn(b'Newer Items', response.data)
    

        
if __name__ == '__main__':
    unittest.main()