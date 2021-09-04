import json

from flask import request
from flask_restful import Resource

from common.models import db, User

class Users(Resource):
    def get(self):
        """Returns a list of all users"""
        users = {}
        for user in User.query.all():
            users[user.id] = user.username
        return {"Users": users}, 200

    def post(self):
        """Creates a user with a given username"""
        data = json.loads(request.get_json())
        username = data["username"]
        user = User.query.filter_by(username=username).first()
        
        if user:
            return {"Status": f"Your user could not be created, a user already exists with the username {username}."}, 400

        if len(username) > 25 :
            return {"Status": f"Your user could not be created, the username is too long."}, 400
        
        user = User(username=username)
        db.session.add(user)
        db.session.commit()

        return {"Status": f"Your user has been created with the username {username}."}, 201

    def delete(self):
        """Deletes a user with a given username"""
        user = User.query.filter_by(username=request.args.get("username")).first()
        if not user:
            return {"Status": "Please include your username as a query parameter. See docs."}, 400

        db.session.delete(user)
        db.session.commit()

        return {
            "Status": f"User deleted",
        }, 200