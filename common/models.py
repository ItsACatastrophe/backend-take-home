from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Many-to-Many relationship table for User and Chat tables
users_chat_table = db.Table("association",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("chat_id", db.Integer, db.ForeignKey("chat.id"), primary_key=True)
)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    messages = db.relationship("Message", backref="chat", lazy=True, cascade="all, delete")
    users = db.relationship(
        "User", 
        secondary=users_chat_table, 
        back_populates="chats",
        lazy="subquery", 
    )

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, default=datetime.now)

    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    recipient_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)

    sent = db.relationship("Message", lazy=True, foreign_keys=[Message.sender_id], cascade="all, delete")
    recieved = db.relationship("Message", lazy=True, foreign_keys=[Message.recipient_id], cascade="all, delete")
    chats = db.relationship(
        "Chat",
        secondary=users_chat_table,
        back_populates="users",
        lazy=True,
        cascade="all, delete",
    )