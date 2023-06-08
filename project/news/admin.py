from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import New

class NewAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title',  'id']

admin.site.register(New, NewAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
