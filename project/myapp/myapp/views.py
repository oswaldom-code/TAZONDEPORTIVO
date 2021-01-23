from django.shortcuts import redirect, render
from django.apps import apps


## Errors Page 404
def handler404(request, *args, **argv):
    return redirect(request, "errors/404.html", {})


## Errors Page 500
def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})


## Errors Page 403
def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})


## Errors Page 400
def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})


def home(request):
    #post = Post.objects.filter(outstandingType1=True)
    QueryModelPost = apps.get_model('blog', 'Post')
    verticalCard = QueryModelPost.objects.filter(
        category=8)[:4]  #category 8 = LVBP
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
