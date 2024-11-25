from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    blog_image = models.ImageField(upload_to='blog_image/', blank=True)
    url = models.URLField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.user}'