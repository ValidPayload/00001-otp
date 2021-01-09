from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("verify-pin", views.verify_pin, name="verify_pin"),
]
