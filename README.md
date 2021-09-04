### A quick note:
My local developing environment uses Winodws so all example commands will be formatted for windows (Usually you can just remove the `python -m` part of the command to translate it to OSX or Linux OS).

In this document:
- [Setup](#setup)
    - [Setup with Pipenv](#setup-with-pipenv)
    - [Setup with Another Virtual Environment](#setup-with-another-virtual-environment)
- [Usage](#usage)
- [Developer's Notes](#developer's-notes)

# Setup

This project was developed using `Python` 3.9.7 and `pipenv` 2021.5.29. These versions are likely not required given the simplicity of the project but they are still listed here in case there is some error. A `Pipfile` and `Pipfile.lock` are both included in this project to make package sync simpler. It's not required to use `pipenv` but it could save you some time.

## Setup with Pipenv

If you choose to utilize pipenv then initializing a virutal environment and installing the required packages should be simple. 

(These commands assume pipenv is already installed)
```
$ python -m pipenv shell
```
Then you can exit the shell and run
```
$ python -m pipenv install
```

There is no differentiation made between developer and standard dependencies for this package so this is all you need to do.

## Setup with Another Virutal Environment

If you're choosing to use another virtual environment (or even install the packages globally) I'll assume you're better aquainted with the commands required to install packages. Just make sure you check the `/Pipfile` for package versions to ensure there's no mismatching.

# Usage

Once the requisite packages are installed, simply run `/app.py`. 

```
$ python -m pipenv run app.py
```

Now that the server is running, you may utilize it's endpoints either by `curl`ing to them or using the included script `/api_test_script.py`. This scripts functionality and usage is better described in `/docs/test_script.md`. The endpoints are documented at `/docs/endpoints.md`.
If a user is ever lost on what objects they've created or what they should do next, the endpoint's `GET` methods are a very helpful way to reorient yourself.

The included tests in `/tests.py` can be run with the following commands:
```
$ python -m pipenv shell
$ python -m unittest discover
```

# Developer's Notes
This section isn't integral to using the project. You can skip to `/docs/endpoints.md` or `/docs/test_script.md` if you haven't already read those yet.

There were a few design choices I thought to include justification/reasoning for here:
- The project directory organization style is meant to mirror the default as suggested by the flask_restful documentation.
- I've tried to make this API representative of something a bit more third-party facing than internal. This is reflected in a few ways:
    - `POST` requests have some notion of "status" feedback (that's meant to be descriptive and user friendly) in addition to their status code.
    - There is a sort of unauthenticated login (see `/docs/test_script.md` and `/docs/endpoints.md` for `username` query parameter).
- The spec was a little bit unclear when it asks for a user to have the ability to retrieve their messages. I interpretted and implemented it as:
    - When a user makes a get request to a chat room they may see messages sent to that chat room by ALL users.
    - When a user makes a get request to the `/data/` endpoint (I thought of this as a sort of data-export use-case) they may see messages send to them by all users. Please note: this does not include messages they've sent (although that may easily be added with a slight refactor).
- The need for URI's that build on themselves never really came about during this project but further down the line I can picture an endpoint such as `/<chat_id>/message/<message_id>` being sent a `DELETE` or `PATCH` request to delete or edit the message's contents.
- In retrospect I should've just used one of those packages that generates endpoint documentation for you.
- If you need to change the default hosting settings of the project, the `api_test_script.py`, `/<chat_id>/` POST error feedback, and `/` get response will be wrong. These values are hard coded.

I've thought of a few next-steps where this project could go (These felt a little out-of-scope of the current project):
- Authentification:
    - When creating a user at the `/users/` endpoint, requesting a password and if a user is successfully created: returning an API token.
    - Store and expect the API token in a header instead of the query parameter.
- Input Validation:
    - Right now validation is in-view and it detracts from readable code, ideally we could migrate this to it's own module of the application.
    - Creating some class-based validators depending on the data type we're expecting would go a long way for code reusability.
    - This starts to sound a lot like html form validation the more I think about it.
- Write more tests:
    - You can never have enough tests (I just didn't want to spend the full 4 hours writing tests).
    - Tests for each endpoint.
    - Tests for database relation object delete cascades.
    - Tests for invalid inputs.
    - Tests for the full integration of the userflow.
    - Tests for input validation.
    - Tests for bug regression.
    - Etc.

As a final note: I had a lot of fun with this project. I really enjoyed building on my knowledge of relational databasing (which I documented in `/docs/database.md`). This was a really enjoyable experience and I'm really happy with what I was able to put together in the time frame I set out with.
=)