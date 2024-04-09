from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from result.models import Account
from . import models
from django.contrib.auth.models import Group


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email','username')
    readonly_fields = ('id', 'date_joined', 'last_login', 'category','groups')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account, AccountAdmin)
admin.site.register(models.ResultDb)

# Create Groups

Student_group = Group.objects.get_or_create(name = 'Students')
Teacher_group = Group.objects.get_or_create(name = 'Teachers')




