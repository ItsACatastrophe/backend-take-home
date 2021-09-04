from flask import Flask
from flask_restful import Api, Resource

from common.models import db
import resources

app = Flask("messenger_api")
app.config.from_object("config")

api = Api(app)
db.init_app(app)

# Routing
api.add_resource(resources.chat.Chats, "/<chat_id>/")
api.add_resource(resources.messenger.Messenger, "/")
api.add_resource(resources.user.Users, "/users/")
api.add_resource(resources.data.Data, "/data/")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=False)