""" Defines URL patterns for the blogs. """

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all blogs
    path('blogs/', views.blogs, name='blogs'),
    # Detail page for a specific blog
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    # New blog  page
    path('new_blog/', views.new_blog, name='new_blog'),
    # New post page for a specific blog
    path('blogs/<int:blog_id>/new_post/', views.new_post, name='new_post'),
    # Edit Posts.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),     
]