# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_app.models import User

admin.site.register(User, UserAdmin)
