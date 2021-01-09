import django_on_heroku
from .settings import *

DEBUG = False

django_on_heroku.settings(locals())
