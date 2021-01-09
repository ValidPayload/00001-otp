from django.db import models

class PIN(models.Model):
	phone_number = models.CharField("phone number", max_length=5)
	pin = models.CharField("pin", max_length=5)
	valid_until = models.DateTimeField("date until pin is valid")
