from django.contrib import admin

# Register your models here.
from .models import Question, UserStatus
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)

admin.site.register(Question)


admin.site.register(UserStatus)
