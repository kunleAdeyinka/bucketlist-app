# tests/test_bucket_items.py

import unittest

from base import BaseTestCase

from project import db
from project.models import User, BucketItem
from io import BytesIO

class BlogPostTests(BaseTestCase):
    
    # ensure a logged in user can add a new post
    def test_user_can_post_bucketitem(self):
        with self.client:
            self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            upload_file = (BytesIO(b'test contents'), "test_image.jpg") 
            response = self.client.post('/addItem', content_type='multipart/form-data', data=dict(title="test item", description="test item", photo=upload_file, private=False, done=False), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'New item was successfully posted. Thanks.', response.data)
            
    #ensure a logged in user is able to go to the delete view
    def test_user_can_delete_bucketitem(self):
        with self.client:
            self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            upload_file = (BytesIO(b'test contents'), "test_image.jpg") 
            response = self.client.post('/addItem', content_type='multipart/form-data', data=dict(title="delete item", description="delete item", photo=upload_file, private=False, done=False), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            bucketitem = db.session.query(BucketItem).filter_by(title="delete item").one()
            url = "/deleteItem/{}/delete/".format(bucketitem.id)
            response = self.client.get(url, follow_redirects=True)
            response = self.client.post(url, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Current BucketList Items', response.data)
    
    # ensure a logged in user can go to the edit item view
    def test_user_can_edit_bucketitem(self):
        with self.client:
            self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            upload_file = (BytesIO(b'test contents'), "test_image.jpg") 
            response = self.client.post('/addItem', content_type='multipart/form-data', data=dict(title="edit item", description="edit item", photo=upload_file, private=False, done=False), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            bucketitem = db.session.query(BucketItem).filter_by(title="edit item").one()
            url = "/editItem/{}/edit/".format(bucketitem.id)
            response = self.client.get(url, follow_redirects=True)
            upload_file = (BytesIO(b'edit contents'), "test_image2.jpg") 
            response = self.client.post('/addItem', content_type='multipart/form-data', data=dict(title="edit items", description="edit items", photo=upload_file, private=False, done=False), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Current BucketList Items', response.data)
    
    # ensure a user not logged  in cannot edit a post
    def test_edititem_route_requires_login(self):
        bucketitem = db.session.query(BucketItem).filter_by(title="Test post").one()
        url = "/editItem/{}/edit".format(bucketitem.id)
        response = self.client.get(url, follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
    
    # ensure a user not logged  in cannot delete a post
    def test_deleteitem_route_requires_login(self):
        bucketitem = db.session.query(BucketItem).filter_by(title="Test post").one()
        url = "/deleteItem/{}/delete".format(bucketitem.id)
        response = self.client.get(url, follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
    
    # enusre pagination exists         

if __name__ == '__main__':
    unittest.main()