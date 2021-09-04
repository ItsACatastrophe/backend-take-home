import json
import os
import requests
import tempfile
import unittest

import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        """Sets up test database and server for each test"""
        app.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db.sqlite3"
        app.app.testing = True
        self.app = app.app.test_client()
        with app.app.app_context():
            app.db.create_all()

    def tearDown(self):
        """Deletes test database for each test"""
        os.remove("test.db.sqlite3")

    def test_create_user(self):
        """Tests creating a user"""
        post_json = json.dumps({"username": "TestingName",})

        res = self.app.post("/users/", json=post_json)
        self.assertEqual(res.status_code, 201)

        res = self.app.get("/users/")
        self.assertIn("TestingName", res.get_json()["Users"].values())

    def test_create_chat(self):
        """Tests creating a chat"""
        post_json = json.dumps({"username": "TestingName1",})
        self.app.post("/users/", json=post_json)

        post_json = json.dumps({"username": "TestingName2",})
        self.app.post("/users/", json=post_json)

        self.app.post("/?username=TestingName1", json=post_json)

        res = self.app.get("/?username=TestingName1")

        self.assertIn("chat with TestingName2", res.get_json()['Chats']['1'].keys())
    
    def test_delete_user(self):
        """Tests deleting a user"""
        post_json = json.dumps({"username": "TestingName",})
        res = self.app.post("/users/", json=post_json)

        res = self.app.delete("/users/?username=TestingName")
        self.assertEqual(res.status_code, 200)

        res = self.app.get("/users/")
        self.assertFalse(res.get_json()["Users"])


if __name__ == "__main__":
    unittest.main()