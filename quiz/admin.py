from django.contrib import admin

from .models import *


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic', 'title', 'create_at']
    list_display_links = ('id', 'title')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'quiz']
    list_display_links = ('id', 'title')
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'right', 'question']
    list_display_links = ('id', 'title')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
