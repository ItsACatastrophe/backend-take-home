from datetime import datetime, timedelta

from common.models import User

def messages_by_date(self, messages_since, sorted_messages):
    """Returns messages with date_created attribute after a given time.

    Keyword arguments:
    messages_since -- date to search for messages after (formatted as <MM-DD-YYYY>)
    sorted_messages -- a sorted iterable containing messages
    """
    messages = []
    
    #This function should only allow for mssages_since arg of <30.
    #We leverage timedelta and dt comparisons to ensure this.
    messages_since = datetime.strptime(messages_since, "%m-%d-%Y")
    thirty_days_since = datetime.now() - timedelta(30)
    messages_since = max(messages_since, thirty_days_since)

    for message in sorted_messages:
        if message.date_created < messages_since:
            break

        sender = User.query.get(message.sender_id)
        messages.append({
            "sender": sender.username,
            "date": message.date_created.strftime("%m-%d-%Y %H:%M:%S:%f"),
            "contents": message.contents,
        })
    return messages

def messages_by_num(self, num, sorted_messages):
    """Returns messages with date_created attribute after a given time.

    Keyword arguments:
    num -- quantity of messages at most to return
    sorted_messages -- a sorted iterable containing messages
    """
    messages = []
    for i in range(min(num, 100)):
        try:
            message = sorted_messages[i]
        except IndexError: #We've gone through all of the messages available
            break

        sender = User.query.get(message.sender_id)
        messages.append({
            "sender": sender.username,
            "date": message.date_created.strftime("%m-%d-%Y %H:%M:%S:%f"),
            "contents": message.contents,
        })
    return messages