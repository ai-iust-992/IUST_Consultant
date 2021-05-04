from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'avatar', 'first_name', 'last_name', 'phone_number']


admin.site.register(UserProfile, UserProfileAdmin)


class ConsultantProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'avatar', 'first_name', 'last_name', 'phone_number', 'accepted']


admin.site.register(ConsultantProfile, ConsultantProfileAdmin)
