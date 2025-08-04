""" Defines URL patterns for accounts."""

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # Include the default auth URLs.
    path('', include('django.contrib.auth.urls')),
]
