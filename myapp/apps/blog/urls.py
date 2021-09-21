from django.urls import path
from .views import blog, detailPost

app_name = 'blog'

urlpatterns = [
    path('', blog, name='homeBlog'),
    path('BEISBOL/VENEZOLANO/LVBP', blog, name='homeLVBP'),
    path('BEISBOL/VENEZOLANO/SEMILLA', blog, name='homeSEMILLA'),
    path('BEISBOL/VENEZOLANO/COMPOTA', blog, name='homeCOMPOTA'),
    path('BEISBOL/VENEZOLANO/PRE-INFANTIL', blog, name='homePREINFANTIL'),
    path('BEISBOL/VENEZOLANO/INFANTIL', blog, name='homeINFANTIL'),
    path('BEISBOL/VENEZOLANO/PRE-JUNIOR', blog, name='homePREJUNIOR'),
    path('BEISBOL/VENEZOLANO/JUNIOR', blog, name='homeJUNIOR'),
    path('BEISBOL/VENEZOLANO/JUVENIL', blog, name='homeJUVENIL'),
    path('BEISBOL/VENEZOLANO/JUEGOS-PARA-HOY', blog, name='homeBlog'),
    path('BEISBOL/VENEZOLANO', blog, name='homeBlog'),
    path('RESULTADOS/BEISBOL/VENEZOLANO/JUEGOS-PARA-HOY',
         blog,
         name='homeBlog'),
    path('RESULTADOS/BEISBOL/VENEZOLANO', blog, name='homeBlog'),
    path('BEISBOL-Y-SU-HISTORIA', blog, name='homeBlog'),
    path('REGLAS-DEL-BEISBOL', blog, name='homeBlog'),
    path('HISTORIA-DEL-BEISBOL', blog, name='homeBlog'),
    path('BEISBOL/QUE-ES', blog, name='homeBlog'),
    path('<slug:slug>/', detailPost, name='detail_post'),
]