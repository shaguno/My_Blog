from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Article(models.Model):

    categorie_article = models.ForeignKey(Categorie, on_delete=models.CASCADE, max_length=100, verbose_name="Categorie Article")
    titre_article = models.CharField(max_length=100, verbose_name="Titre Article")
    synopsis_article = models.CharField(max_length=180, verbose_name="Synopsis Article")
    auteur_article = models.CharField(max_length=60, verbose_name="Auteur Article")
    date_creation_article = models.DateTimeField(auto_now_add=True, verbose_name="Date Article")
    contenu_article = models.TextField(verbose_name="Contenu Article")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.titre_article