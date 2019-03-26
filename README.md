# Badges

[![Build Status](https://travis-ci.org/Ivankivu/EPIC-mail.svg?branch=user-delete-email-inbox-164727466)](https://travis-ci.org/Ivankivu/EPIC-mail)
[![Maintainability](https://api.codeclimate.com/v1/badges/079ceee6c85bf2c40de9/maintainability)](https://codeclimate.com/github/Ivankivu/EPIC-mail/maintainability) [![Coverage Status](https://coveralls.io/repos/github/Ivankivu/EPIC-mail/badge.svg?branch=api-user-get-all-sent-emails-164727371)](https://coveralls.io/github/Ivankivu/EPIC-mail?branch=api-user-get-all-sent-emails-164727371)
[![codecov](https://codecov.io/gh/Ivankivu/EPIC-mail/branch/user-delete-email-inbox-164727466/graph/badge.svg)](https://codecov.io/gh/Ivankivu/EPIC-mail)

## Welcome to EPIC Mail

The internet is increasingly becoming an integral part of lives. Ever since the invention of
[electronic mail](https://en.wikipedia.org/wiki/Email) by [Ray Tomlinson](https://en.wikipedia.org/wiki/Ray_Tomlinson), emails have grown to become the primary medium of
exchanging information over the internet between two or more people, until the advent of Instant
Messaging (IM) Apps.

As EPIC Andelans who work towards advancing human potential and giving back to the society,
we wish to empower others by building a web app that helps people exchange
messages/information over the internet.

## UI Features

 |`/user`| ``|
 |---|---|
 |- signup for a new EPIC Mail account| - create groups|
 |- sign into my EPIC Mail account| - add individuals to groups|
 |- reset password||
 |- view inbox||
 |- reade email message||
 |- view sent messages and retract a sent message||
 |- send email to individuals or groups||

## login details

|user account|Admin account|
|:---:|:---:|
|email  `ivan@gmail.com`|email  `admin@andela.ug`|
|password  `uganda`|password  `andela256`|


## Built-with

* [HTML5](https://en.wikipedia.org/wiki/HTML) - Hypertext Markup Language for creating web pages and web applications.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Cascading Style Sheets, a styling language used beautifying and adding style to an [HTML](https://en.wikipedia.org/wiki/HTML) page
* [Javascript](https://en.wikipedia.org/wiki/JavaScript) - a high level programming language thats used to apply dynamism to elements on a web page or web application.

To get started in order to view the application, Follow this [Demo](https://ivankivu.github.io/EPIC-mail/UI/)

## EPIC mail API v1

## Heroku [Demo](https://epicmail-v1.herokuapp.com/)

* copy the above url to any tool of your choice for like [Postman](https://www.getpostman.com/)
* use the sample json data below to get started

```create message
{
 "reciverId": 2,
  "subject": "food",
 "message": "Hi!, tom. Please buy kikomando"
}
```

```create user
{
 "firstname": "ivan",
 "lastname": "kivumbi",
 "email": "ivan@gmail.com",
 "password: "brenda226"
}
```

### Prerequisites

What things you need to install the software

```python
* Python [3.6](https://www.python.org/downloads/release/python-367/) and later- Programming language that lets you work more dynamically
* Flask - Python based web framework thats rich with dependecy support
* Virtualenv - A virtual environment for Running the tests
```

### Installation

Clone this Repository

[clone this](https://github.com/Ivankivu/EPIC-mail.git)

$ Then select develop branch

Clone this Repository

$ https://github.com/Ivankivu/EPIC-mail

$  `cd EPIC-mail`, 
$ create a virtual environment `virtualenv env`

### on windows

$ source /env/Scripts/
$ source activate

### on linux

$ source env/bin/activate
$ Then, install all the necessary dependencies by  `pip install -r requirements.txt

### Run app by

Run the server At the terminal or console type

$ Python run.py

## Running the tests

This project is composed with continuous intergration thus on every repository activity like Push, pull requests testing is done
with Travis CI, coveralls for test coverage and codeclimate for maintainability.

Tests can be run locally with the following commands:

* pytest -m unittest
* pytest -v --cov app --cov-report term-missing
* pytest -v --with-coverage

## API routes and their actions

| ENDPOINT | ROUTE | FUNCTIONALITY |NOTES]
| ------- | ----- | ------------- |-------|
| POST | [/api/v1/auth/signup](https://epicmail-v1.herokuapp.com/api/v1/auth/signup) | The user can signup a new account| |
| POST | [/api/v1/auth/login](https://epicmail-v1.herokuapp.com/api/v1/auth/login) | The user can login with valid credentials| |
| POST | [/api/v1/messages](https://epicmail-v1.herokuapp.com/api/v1/messages) |The user can create and send a message| |
| GET |[/api/v1/messages](https://epicmail-v1.herokuapp.com/api/v1/messages)| Only the can get all user's' messages recieved||
| GET |[/api/v1/messages/(int:messageId)](https://epicmail-v1.herokuapp.com/api/v1/messages/1)| user can get a specific user's message by ID||
| GET |[/api/v1/messages/unread](https://epicmail-v1.herokuapp.com/api/v1/messages/unread)| user can get all user's unread messages||
| GET |[/api/v1/messages/sent](https://epicmail-v1.herokuapp.com/api/v1/messages/sent)| user can get all user's sent messages||
| DELETE |[/api/v1/messages/(int:messageId)](https://epicmail-v1.herokuapp.com/api/v1/messages/1)| user can delete a specific user's message by ID||

## Authors

* **Ivan Kivumbi** - *Initial work* - [FastFoodFast](https://github.com/Ivankivu/Fast-Food-Fast) | [Sendit](https://github.com/Ivankivu/SendIT)

## Acknowledgments

* We warmly welcome comments and reviews
