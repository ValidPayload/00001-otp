import django_on_heroku
from .settings import *

DEBUG = True

django_on_heroku.settings(locals())
