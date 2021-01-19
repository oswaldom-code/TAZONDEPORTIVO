from django.contrib import admin
from django.conf import settings  # Servir imagenes en desarrollo
from django.conf.urls.static import static  # Servir imagenes en desarrollo
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('NOTICIAS/',
         include(('apps.blog.urls', 'beisbol_blog'), namespace='blog')),
    path('ARTICULOS/',
         include(('apps.blog.urls', 'beisbol_blog'), namespace='blog')),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)  # Servir imagenes en desarrollo
