from django.shortcuts import render

# Create your views here.

import logging
from cars.models import Car
from django.views.generic import ListView
from .filters import CarFilter

menu = [{'title': "About car showroom", 'url_name': 'about'},
        {'title': "Buy car", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Log in", 'url_name': 'login'}]


class CarView(ListView):
    model = Car
    template_name = 'index.html'
    context_object_name = 'cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['filter'] = CarFilter(self.request.GET, queryset=self.get_queryset())
        return context




