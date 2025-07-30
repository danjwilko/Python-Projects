"""Defines URL patterns for the meal_planner app."""

from django.urls import path

from . import views

app_name = 'meal_plans'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Other meal planner URLs can be added here.
]