from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'firstName', 'lastName', )
    list_filter = ('firstName', 'lastName', 'id')
    search_fields = ('email', 'firstName', 'lastName')
    ordering = ('id',)




