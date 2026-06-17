from django.contrib import admin

from sections.models import Section, Content


# Register your models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id','title', )
    list_filter = ('title', )
    search_fields = ('title', )
    ordering = ('id',)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'section', )
    list_filter = ('title', 'section', )
    search_fields = ('title', 'section', )
    ordering = ('id', 'section',)

