from django.shortcuts import render
from .models import Post

def blog(request):
    query = Post.objects.filter(state=True).order_by('-creationDate')
    posts = query
    data = {
        'post': posts,
        'appId'            : '795049488022092',
        'autoLogAppEvents' : True,
        'xfbml'            : True,
        'version'          : 'v9.0'
    }
    return render(request, 'blog/index.html', data )

def detailPost(request, slug):
    query = Post.objects.get(slug = slug)
    data = {
        'post' : query
    }
    return render(request, 'blog/detail.html', data)


