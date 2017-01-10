# tests/test_bucket_items.py

import unittest

from base import BaseTestCase

from project import db
from project.models import User, BucketItem

class BlogPostTests(BaseTestCase):
    
    # ensure a logged in user can add a new post
    def test_user_can_post_bucketitem(self):
        with self.client:
            self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            response = self.client.post('/addItem', data=dict(title="test", post="test"), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'New item was successfully posted. Thanks.', response.data)
            
    #ensure a logged in user can delete a post
    def test_user_can_delete_bucketitem(self):
        with self.client:
            self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            response = self.client.post('/addItem', data=dict(title="delete item", post="delete item"), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            bucketitem = db.session.query(BucketItem).filter_by(title="delete item").one()
            url = "/deleteItem/{}/delete".format(bucketitem.id)
            response = self.client.get(url, follow_redirects=True)
            self.assertIn(b'delete item', response.data)
    
    # ensure a logged in user can edit a post
    def test_user_can_edit_bucketitem(self):
        with self.client:
            self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            response = self.client.post('/addItem', data=dict(title="edit item", post="edit item"), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            bucketitem = db.session.query(BucketItem).filter_by(title="edit item").one()
            url = "/editItem/{}/edit".format(bucketitem.id)
            response = self.client.get(url, follow_redirects=True)
            self.assertIn(b'edit item', response.data)
    
    # ensure a user not logged  in cannot edit a post
    def test_edititem_route_requires_login(self):
        bucketitem = db.session.query(BucketItem).filter_by(title="Test post").one()
        url = "/editItem/{}/edit".format(bucketitem.id)
        response = self.client.get(url, follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
    
    # ensure a user not logged  in cannot delte a post
    def test_deleteitem_route_requires_login(self):
        bucketitem = db.session.query(BucketItem).filter_by(title="Test post").one()
        url = "/deleteItem/{}/delete".format(bucketitem.id)
        response = self.client.get(url, follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
            

if __name__ == '__main__':
    unittest.main()