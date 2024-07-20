from django.contrib import admin
from account.models import Account
class accountAdim(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name')
    list_display_links = ('username', 'email')

admin.site.register(Account, accountAdim)
