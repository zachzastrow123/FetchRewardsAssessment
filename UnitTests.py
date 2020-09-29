from flask import Flask
import unittest
import json
from Assessment import app


class ApiTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_pyramid(self):
        response = self.app.post('/pyramid',
                                 data="banana",
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('UTF-8'), "True")

    def test_not_pyramid(self):
        response = self.app.post('/pyramid',
                                 data="bandana",
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('UTF-8'), "False")

    def test_get_request(self):
        response = self.app.get('/pyramid')
        self.assertEqual(response.status_code, 405)


if __name__ == "__main__":
    unittest.main()
