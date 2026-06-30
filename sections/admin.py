from django.contrib import admin

from sections.models import Section, Content, Question


# Register your models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_filter = ('title', )
    search_fields = ('title', )
    ordering = ('id', )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'section', )
    list_filter = ('title', 'section', )
    search_fields = ('title', 'section', )
    ordering = ('id', 'section', )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'answer', )
    list_filter = ('section', )
    ordering = ('id', 'section', )
    search_fields = ('question', )
