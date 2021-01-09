# Valid Payload 00001 - OTP

A Django application meant to demonstrate common vulnerabilities in OTP validation. It can be easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article.

## Running Locally

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.local.txt

$ python manage.py migrate
$ python manage.py runserver
```

The app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
