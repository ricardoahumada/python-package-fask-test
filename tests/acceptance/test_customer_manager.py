import base64
import unittest
import json
from app import app


class TestApp(unittest.TestCase):
    token=''

    def test_1_get_none(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/customers/', content_type='application/json')
        # print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, None)

    def test_2_post(self):
        tester = app.test_client(self)
        test_data = {"address": "5 Spenser Plaza",
                     "email": "kbraksper0@mac.com",
                     "name": "Kelbee"}
        response = tester.post('/api/v1/customers/',content_type='application/json', json=test_data)
        # print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, None)

    def test_3_get_none(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/customers/', content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data)>0)

    def test_4_testToken(self):
        tester = app.test_client(self)
        test_data = {"email":"user@test.com","password":"passwordjd"}
        response = tester.post('/api/v1/token',content_type='application/json', json=test_data)        
        print(response.json)
        self.assertEqual(response.status_code, 200)
        if response.status_code==200:
            TestApp.token=response.json['token']
        
    def test_5_get_restricted(self):
        tester = app.test_client(self)
        print(f"token: {self.token}")
        headers = {"Authorization": f"Bearer {TestApp.token}"}

        response = tester.get('/api/v1/restricted', content_type='application/json', headers=headers)
        print(response.json)
        self.assertEqual(response.status_code, 200)
