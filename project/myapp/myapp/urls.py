from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('NOTICIAS/',
         include(('apps.blog.urls', 'beisbol_blog'), namespace='blog')),
    path('ARTICULOS/',
         include(('apps.blog.urls', 'beisbol_blog'), namespace='blog')),
    url(r'^$', home, name='home'),
]

handler404 = 'myapp.views.handler404'