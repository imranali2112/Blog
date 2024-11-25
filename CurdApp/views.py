from django.shortcuts import render, redirect
from .import models
from django.contrib import messages

# Create your views here.
def index(requests):
    about = models.About.objects.all()

    return render(requests, 'index.html', {'about':about})


def blog(requests):
    if requests.method == 'POST':
        user = requests.user
        title = requests.POST['title']
        content = requests.POST['content']
        blog_image = requests.FILES['blog_image']
        url = requests.POST['url']
        models.Blog.objects.create(user = user, title = title, content = content, blog_image = blog_image, url = url)
        messages.success(requests, message='Your blog is uploded successfully')
        return redirect('index')
    
    return render(requests, 'blog.html', {'blog': blog})

def blog_list(requests):
    blogs = models.Blog.objects.all()
    return render(requests, 'blog_list.html', {'blogs': blogs})

def blog_detail(requests, blog_id):
    blogs = models.Blog.objects.get(id = blog_id)
    return render(requests, 'blog_detail.html', {'blogs':blogs})

def blog_delete(requests, blog_id):
    blogs = models.Blog.objects.get(id = blog_id)
    if requests.method == 'POST':
        blogs.delete()
        messages.success(requests, message='Your blog is deleted is sucessfully')
        return redirect('blog_list')
    return render(requests, 'blog_delete.html', {'blogs':blogs})

def blog_update(requests, blog_id):
    blogs = models.Blog.objects.get(id = blog_id)
    if requests.method == 'POST':
        blogs.title = requests.POST.get('title','')
        blogs.content = requests.POST.get('content','')
        if requests.FILES.get('blog_image'):
            blogs.blog_image = requests.FILES['blog_image']
        blogs.url = requests.POST.get('url','')
        blogs.save()
        return redirect('blog_list')
    
    return render(requests, 'blog_update.html',{'blogs': blogs})
