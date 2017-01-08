# tests/test_bucket_items.py

import unittest

from base import BaseTestCase

class BlogPostTests(BaseTestCase):
    
    # ensure a logged in user can add a new post
    def test_user_can_post_bucketitem(self):
        with self.client:
            self.client.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
            response = self.client.post('/addItem', data=dict(title="test", post="test"), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'New item was successfully posted. Thanks.', response.data)
            

if __name__ == '__main__':
    unittest.main()