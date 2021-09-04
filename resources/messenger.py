import json

from flask import request
from flask_restful import Resource

from common.models import db, Chat, User


class Messenger(Resource):
    def get(self):
        """Returns a list of chats that a given user has access to."""
        user = User.query.filter_by(username=request.args.get("username")).first()
        if not user:
            return {"Status": "Please include your username as a query parameter. See docs."}, 400

        chats = {}
        for chat in Chat.query.all():
            if user in chat.users:
                recipient = set(chat.users).difference({user}).pop() #Use difference of sets to find non-self user in chat

                chats[chat.id] = {
                    f"chat with {recipient.username}": {
                        "uri" :  f"http://127.0.0.1:5000/{chat.id}/"
                    }
                }

        return {"Chats": chats}

    def post(self):
        """Creates a chat room for a given user with a given user"""
        data = json.loads(request.get_json())

        recipient = User.query.filter_by(username=data["username"]).first()
        if not recipient:
            return {"Status": "There are no users with that username. Please create this user first."}, 400

        sender = User.query.filter_by(username=request.args.get("username")).first()
        if not sender:
            return {"Status": "Please include your username as a query parameter. See docs."}, 400

        if recipient.id == sender.id:
            return {"Status": "Please don't create a chat room with yourself. I didn't plan for the implications of thats."}, 400

        chat = Chat(
            users=[sender, recipient]
        )
        db.session.add(chat)
        db.session.commit()

        return {
            "Status": f"Your chat has been created with the user: {recipient.username}",
            "uri": f"http://127.0.0.1:5000/{chat.id}/"
        }, 201

    def delete(self):
        """Deletes a chat room with a given id"""
        data = json.loads(request.get_json())
        chat = Chat.query.get(data["id"])
        if not chat:
            return {"Status": "This chat doesn't appear to exist."}, 400

        db.session.delete(chat)
        db.session.commit()
        return {
            "Status": f"Chat deleted",
        }, 200