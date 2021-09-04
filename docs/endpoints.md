This projects endpoints are (ordered by logical flow):
- [/users/](#/users/)
    - GET
    - POST
    - DELETE
- [/](#/)
    - GET
    - POST
    - DELETE
- [/<chat_id>/](#/<chat_id>/)
    - GET
    - POST
- [/data/](#/data/)
    - GET

# /users/

This endpoint is responsible for listing (`GET`), creating (`POST`), and deleteing (`DELETE`) users.

## GET

This request method expects nothing more than a `GET` request. It returns a dictionary of `user.id`'s as keys and `user.username`'s as values. It's worth noting that we only ever use `user.username` when identifying a user. `user.id` is displayed but not entirely necessary.

## POST

This request method expects a `POST json` of:
```
{
    username: <str>
}
```

The username is the desired `user.username` of the `user` you'd like to create. This must be less than 25 characters long and must be unique across all usernames of `user`s. This username is what you'll use to "log in" with (using this value as a query parameter e.g. `/?username=MyUserName`).

## DELETE

This request method expects a query parameter of your username. The user whose `user.username` is the same as your query parameter will be deleted.

# /

This endpoint is responsible for listing (`GET`), creating (`POST`), and deleting (`DELETE`) chats.

## Get

This request method expects a query parameter of your username. It returns a dictionary of `chat.id`'s as keys and a nested dictionary as a value. This nested dictionary contains keys of strings identifying who the chat is with and values of the chat's URI. This request method may be used at any time 

## POST

This request method expects a `POST json` of:
```
{
    username: <str>
}
```

The username is the `user.username` of the `user` you'd like to create a chat with. The URI of the chat created is returned in the response json. This is the same as the `/<chat_id>/` endpoint.

## DELETE

This request method expects a `POST json` of:
```
{
    id: <int>
}
```

The id is the `chat.id` of the `chat` you'd like to delete. This id can be retrieved from a `GET` request to this endpoint.

# /<chat_id>/

This endpoint is responsible for listing (`GET`), and sending (`POST`) message in a given chat.

## GET

This request method expects a query parameter of **either** `num=<int>` or `after=<MM-DD-YYYY>`. If both are supplied then `after=<MM-DD-YYYY>` is defaulted to (because it usually will return more messages in practical use). The `num=<int>` parameter indicates how many messages you would like to view in the history where `<int>` caps out at 100. The `after=<MM-DD-YYYY>` parameter indicates messages after a given date should be shown. The time is initialized to the very start of the day so messages sent the day specified **are** included. If a time of > 30 days ago is given then 30 days prior to today is used instead (presumably to reduce potential stress on the database for large queries).

## POST

This request method expects a `POST json` of:
```
{
    message: <str>
}
```

The message is the `message.contents` of the message you would like to send to the other user in the chat. The `message.contents` must be less than 200 characters long.
This request method also expects a query parameter of your username.

# /data/

This endpoint is responsible for listing (`GET`) messages sent to a user.

## GET

his request method expects a query parameter of **either** `num=<int>` or `after=<MM-DD-YYYY>`. If both are supplied then `after=<MM-DD-YYYY>` is defaulted to (because it usually will return more messages in practical use). The `num=<int>` parameter indicates how many messages you would like to view in the history where `<int>` caps out at 100. The `after=<MM-DD-YYYY>` parameter indicates messages after a given date should be shown. The time is initialized to the very start of the day so messages sent the day specified **are** included. If a time of > 30 days ago is given then 30 days prior to today is used instead (presumably to reduce potential stress on the database for large queries).
This request method also expects a query parameter of your username.