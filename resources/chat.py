import json

from datetime import datetime
from flask import request
from flask_restful import Resource

from common.models import db, Chat, Message, User
from common.utils import messages_by_date, messages_by_num


class Chats(Resource):
    def get(self, chat_id):
        """Returns a list of messages in a chat according to query parameters."""

        chat = Chat.query.get(chat_id)
        sorted_messages = sorted(chat.messages, key=lambda x: x.date_created)
        
        num = request.args.get("num")
        messages_since = request.args.get("after")
        if messages_since:
            messages = messages_by_date(self, messages_since, sorted_messages)
        elif num:
            messages = messages_by_num(self, int(num), sorted_messages)
        else:
            return {"Status": "Please include a query string. See docs."}, 400

        return {"Messages": messages}, 200

    def post(self, chat_id):
        """Sends a message in a chat."""
        data = json.loads(request.get_json()) #Dict rep. of json body
        
        sender = User.query.filter_by(username=request.args.get("username")).first()
        if not sender:
            return {"Status": "Please include your username as a query parameter. See docs."}, 400

        chat = Chat.query.get(chat_id)
        if not chat:
            return {"Status": "This chat doesn't exist. Please navigate to http://127.0.0.1:5000/ and create one."}, 400

        if len(data["message"]) > 200:
            {"Status": "This message is too long. Please break your message up into multiple requests."}, 400
        
        recipient = set(chat.users).difference({sender}).pop() #Use difference of sets to find non-self user in chat
        message = Message(
            contents=data["message"],
            sender_id=sender.id,
            recipient_id=recipient.id,
            chat_id=chat.id,
        )
        chat.messages.append(message)

        db.session.add(message)
        db.session.commit()
        return {"Status": "Your message has been sent!"}, 201