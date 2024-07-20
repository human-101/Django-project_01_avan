from django.urls import path
from food.views import *

app_name = 'food'

urlpatterns = [
    path('food/', FoodMain.as_view(), name='food_main'),
    path('food/list/', ListFood.as_view(), name='list'),
    path('food/nonveg/', ListNonVeg.as_view(), name='nonveg'),
path('food/veg/', ListVeg.as_view(), name='veg'),
path('food/update/<slug:slug>', FoodUpdateView.as_view(), name='update'),
path('food/remove/<slug:slug>', FoodRemoveView.as_view(), name='remove'),
path('food/recipe/<int:pk>/', Recipe.as_view(), name='recipe'),
    path('food/create/', CreateFood.as_view(), name='create')
]