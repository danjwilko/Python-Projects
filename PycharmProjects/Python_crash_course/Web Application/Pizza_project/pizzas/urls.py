"""Defines the URL patterns for pizza"""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Pizzas page.
    path('pizza/', views.pizza, name='pizza'),
    # Pizza details page.
    path('pizza/<int:pizza_id>/', views.toppings, name='toppings'),
]