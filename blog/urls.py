from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/A/', views.voir_categorie_generative, name='voir_categorie_generative'),
    path('blog/IA_image/', views.voir_categorie_image, name='categorie_image'),
    path('blog/IA_musique/', views.voir_categorie_musique, name='categorie_musique'),
    path('blog/IA_coding/', views.voir_categorie_coding, name='categorie_coding'),
    path('blog/IA_autres/', views.voir_categorie_autres, name='categorie_autres'),
]

