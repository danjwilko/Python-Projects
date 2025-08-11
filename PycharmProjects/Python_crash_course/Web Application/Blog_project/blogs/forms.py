from django import forms

from .models import Blog, Post

class BlogForm(forms.ModelForm):
    """Form for creating or updating a blog."""
    
    class Meta:
        model = Blog
        fields = ['title', 'text']
        labels = {'text':'Blog Title','text':'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Single line
            'text': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'})  # Smaller textarea
        }
        
class PostForm(forms.ModelForm):
    """Form for creating or updating a post."""
    
    class Meta:
        model = Post
        fields = ['title', 'text']
        labels = {'text':'Post Title','text':'Content'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Single line
            'text': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'})  # Smaller textarea
        }