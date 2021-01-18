from django.shortcuts import render
from .models import Post


def blog(request):
    queryPost = Post.objects.filter(state=True)
    context = {
        'post': queryPost,
        'appId': '795049488022092',
        'autoLogAppEvents': True,
        'xfbml': True,
        'version': 'v9.0'
    }
    return render(request, 'blog/index.html', context)


def detailPost(request, slug):
    query = Post.objects.get(slug=slug)
    context = {'post': query}
    return render(request, 'blog/detail.html', context)
