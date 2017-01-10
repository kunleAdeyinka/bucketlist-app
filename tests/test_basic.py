# tests/test_basic.py

import unittest

from flask.ext.login import current_user

from base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that main page loads
    def test_main_route_loads(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'welcome to mustdolistapp', response.data)

    # Ensure that welcome page loads
    def test_index_route_works_as_expected(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'welcome to mustdolistapp', response.data)

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
        response = self.client.post('/login', data=dict(username="admin", password="admin"),follow_redirects=True)
        self.assertIn(b'Test post', response.data)



if __name__ == '__main__':
    unittest.main()