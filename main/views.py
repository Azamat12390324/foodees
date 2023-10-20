from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView, DeleteView,DetailView,View


class Home(TemplateView):
    template_name = 'main/home.html'
