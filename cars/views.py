from typing import Any
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

from django.views.generic import ListView, CreateView

# Create your views here.    
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = Car.objects.filter(model__icontains = search)

        return cars

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars'
    