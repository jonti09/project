from django.contrib import admin
from Notification.models import ToiNews, Weather, Help

# Register your models here.

admin.site.register(ToiNews)
admin.site.register(Weather)
admin.site.register(Help)
