from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Categorie


def index(request):
    return render(request, 'blog/index.html')


def blog(request):
    articles = Article.objects.order_by('-date_creation_article')
    return render(request, 'blog/blog.html', {'articles': articles})


def voir_categorie_generative(request, ):
    cat = Categorie.objects.filter()
    articles = Article.objects.all()
    return render(request, 'blog/categorie_generative.html', {'articles': articles, 'cat': cat})


def voir_categorie_image(request):
    articles = Article.objects.all()
    categorie = Categorie.objects.all()
    return render(request, 'blog/categorie_image.html', {'categorie': categorie, 'articles': articles})


def voir_categorie_musique(request):
    return render(request, 'blog/categorie_musique.html')


def voir_categorie_coding(request):
    return render(request, 'blog/categorie_coding.html')


def voir_categorie_autres(request):
    return render(request, 'blog/categorie_autres.html')


