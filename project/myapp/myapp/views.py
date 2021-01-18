from django.shortcuts import render
from django.apps import apps


def home(request):
    #post = Post.objects.filter(outstandingType1=True)
    QueryModelPost = apps.get_model('blog', 'Post')
    verticalCard = QueryModelPost.objects.filter(category=8)[:4] #category 8 = LVBP
    outstandingType1 = QueryModelPost.objects.filter(outstandingType1=True)
    outstandingType2 = QueryModelPost.objects.filter(outstandingType2=True)
    QueryBlackboardResults = apps.get_model('blog', 'BlackboardResults')
    Results = QueryBlackboardResults.objects.filter(state=True)
    context = {
        'verticalCard': verticalCard,
        'post': outstandingType1,
        'postHot': outstandingType2,
        'results': Results
    }
    return render(request, 'index.html', context)
