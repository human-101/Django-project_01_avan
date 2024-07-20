# For Generating URLs
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from food.forms import FoodForm
# Category Objects in Django
from food.models import Food
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect



class FoodMain(ListView):
    model = Food
    template_name = 'food/layout.html'
    context_object_name = 'foods'

class ListFood(ListView):
    model = Food
    template_name = 'food/list.html'
    context_object_name = 'foods'

class ListNonVeg(ListView):
    model = Food
    template_name = 'food/Non-veg.html'
    context_object_name = 'foods'
class ListVeg(ListView):
    model = Food
    template_name = 'food/Veg.html'
    context_object_name = 'foods'

class FoodUpdateView(SuccessMessageMixin, UpdateView):
    model = Food
    template_name = 'food/create.html'
    form_class = FoodForm
    success_url = reverse_lazy('food:list')
    extra_context = {'job': 'Update'}
    success_message = "Category updated successfully."

class FoodRemoveView(DeleteView):
    model = Food
    template_name = 'food/remove.html'
    success_url = reverse_lazy('food:list')

class CreateFood(SuccessMessageMixin, CreateView):
    model = Food
    template_name = 'food/create.html'
    form_class = FoodForm
    success_url = reverse_lazy('food:list')
    extra_context = {'job': 'Create'}
    success_message = "Category created successfully."

class Recipe(DetailView):
    model = Food
    template_name = 'food/recipe.html'
    context_object_name = 'foods'
