from django.contrib import admin
from .models import ChatGroup
from .models import GroupMessage

# Register your models here.

admin.site.register(ChatGroup)
admin.site.register(GroupMessage)
