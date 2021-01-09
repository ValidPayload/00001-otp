from django.contrib import admin
from .models import PIN


class PINAdmin(admin.ModelAdmin):
	pass


admin.site.register(PIN, PINAdmin)
