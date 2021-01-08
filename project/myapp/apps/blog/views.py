from django.shortcuts import render
from .models import Post

def blog(request):
    posts = Post.objects.filter(state=True)
    data = {
        'post': posts
    }
    return render(request, 'blog/index.html', data)

