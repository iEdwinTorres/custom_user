from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_user_app.models import MyUser

admin.site.register(MyUser, UserAdmin)