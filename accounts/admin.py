from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'data_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('last_login', 'data_joined')
    ordering = ('-data_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)