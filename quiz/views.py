from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class HomeView(ListView):
    model = Quiz
    template_name = 'quiz/home.html'
    context_object_name = 'quizes'

    # def get_context_data(self, **kwargs):
    #     # создаем контекст, передаем аргументы
    #     context = super().get_context_data(**kwargs)
    #     # добавляем в контекст form
    #     context['amount'] = len(Quiz.get_questions())
    #     # возвращаем контекст
    #     return context
