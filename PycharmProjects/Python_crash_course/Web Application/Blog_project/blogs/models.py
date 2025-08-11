from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    """A blog."""
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.title
    
class Post(models.Model):
    """A post in a blog."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # Optional: add post titles
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'posts'
    
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        else:
            return self.text