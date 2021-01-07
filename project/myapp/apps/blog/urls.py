
from django.urls import path
from .views import blog

urlpatterns = [
    path('', blog, name= 'blog'),
    #path('<slug:slug>', detailpost, name= 'detailpost'),
    #path('allpost/', allPost, name= 'allPost'),
]