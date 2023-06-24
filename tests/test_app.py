import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_word(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.get_data(as_text=True), 'Test')

    def test_admin_portal(self):
        response = self.client.post('/admin', data={'new_word': 'New Test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Portal', response.data)
        self.assertIn(b'New Word:', response.data)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New Test', response.data)

        response = self.client.post('/admin', data={'new_word': 'Test'})
        self.assertEqual(response.status_code, 200)
        


if __name__ == '__main__':
    unittest.main()
