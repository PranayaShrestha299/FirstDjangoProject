from django.contrib import admin

# Register your models here.

from .models import Room,Topic,Message
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Room)
