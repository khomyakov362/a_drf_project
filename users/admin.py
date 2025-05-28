from django.contrib import admin
from users import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'last_name', 'first_name')
    list_filter = ('id', 'email')
    ordering = ('id',)
