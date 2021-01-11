from django.urls import path
from .views import blog, detailPost

app_name = 'blog'

urlpatterns = [
    path('', blog, name= 'inicio'),
    path('<slug:slug>/', detailPost, name= 'detail_post'),

]