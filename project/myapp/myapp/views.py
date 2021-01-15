from django.shortcuts import render
from django.apps import apps


def home(request):
    #post = Post.objects.filter(outstandingType1=True)
    ModelPost = apps.get_model('blog', 'Post')
    verticalCard = ModelPost.objects.filter(category=8)[:4]
    outstandingType1 = ModelPost.objects.filter(outstandingType1=True)
    outstandingType2 = ModelPost.objects.filter(outstandingType2=True)
    context = {
        'verticalCard' : verticalCard,
        'post': outstandingType1,
        'postHot': outstandingType2
    }
    return render(request, 'index.html', context)
