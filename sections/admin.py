from django.contrib import admin
from sections import models

@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    ordering = ('id',)

@admin.register(models.SectionContent)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'title')
    list_filter = ('section',)
    ordering = ('id', 'section')

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'question', 'description', 'answer')
    list_filter = ('section',)
    ordering = ('id', 'section')