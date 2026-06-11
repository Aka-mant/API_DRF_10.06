from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstName', 'lastName', )
    list_filter = ('role', 'is_active', 'id')
    search_fields = ('email', 'firstName', 'lastName')
    ordering = ('id',)




