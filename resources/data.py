import json

from flask import request
from flask_restful import Resource

from common.models import Message, User
from common.utils import messages_by_date


class Data(Resource):
    def get(self):
        """Returns a list of messages sent to a user according to query parameters.W"""
        user = User.query.filter_by(username=request.args.get("username")).first()
        if not user:
            return {"Status": "Please include your username as a query parameter. See docs."}, 400

        messages = []

        sorted_messages = Message.query.filter_by(recipient_id=user.id).order_by(Message.date_created)
        num = request.args.get("num") or 0 #Handles num not included in the query string
        messages_since = request.args.get("after")
        if messages_since:
            messages = messages_by_date(self, messages_since, sorted_messages.all())
        elif num:
            #We have the opportunity to use a size-limited query instead of
            #common.utils.messages_by_num, saving us some resources.
            sorted_messages = sorted_messages.limit(min(int(num), 100)).all()
            for message in sorted_messages:

                sender = User.query.get(message.sender_id)
                messages.append({
                    "sender": sender.username,
                    "date": message.date_created.strftime("%m-%d-%Y %H:%M:%S:%f"),
                    "contents": message.contents,
                })
        else:
            return {"Status": "Please include a query string. See docs."}, 400

        return {"Messages": messages}, 200