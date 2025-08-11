from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, Post
from .forms import BlogForm, PostForm


# Create your views here.
def index(request):
    """The home page for the blog."""
    return render(request, 'blogs/index.html')

@login_required
def blogs(request):
    """Show a list of blogs."""
    blogs = Blog.objects.filter(owner=request.user).order_by('-date_added') # Only show blogs owned by the current user
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

@login_required
def blog(request, blog_id):
    """Show all posts for current blog."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.all().order_by('-date_added')  # Only this blog's posts
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/posts.html', context)

@login_required
def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')  # Redirect to the list of blogs

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_post(request, blog_id):
    """Add a new post to a blog."""
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)  # Don't save to the database yet
            new_post.blog = blog  # Associate the post with the blog
            new_post.save()  # Now save it
            return redirect('blogs:blog', blog_id=blog.id)  # Redirect to the blog's detail page

    # Display a blank or invalid form.
    context = {'form': form, 'blog': blog}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """ Edit an existing post."""
    post = Post.objects.get(id=post_id)
    blog = post.blog  # Get the blog associated with the post
    if blog.owner != request.user:
        raise Http404("You do not have permission to edit this post.")

    if request.method != 'POST':
        # Initial request; pre-fill form with the current post data.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()  # Save the updated post
            return redirect('blogs:blog', blog_id=blog.id)  # Redirect to the blog's detail page

    # Display a blank or invalid form.
    context = {'form': form, 'post': post, 'blog': blog}
    return render(request, 'blogs/edit_post.html', context)