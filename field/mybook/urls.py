# Importation de la fonction 'path' qui permet de définir des routes URL dans Django
from django.urls import path

# Importation de la vue 'liste_livres' depuis le fichier views.py du même répertoire
from .views import liste_livres

# Définition de la liste des URL disponibles dans cette application
urlpatterns = [
    # Création d'une route URL : quand l'utilisateur accède à '/livres/',
    # Django appelle la vue 'liste_livres' pour générer la réponse
    # Le nom 'livres_liste' permet de référencer cette URL ailleurs dans le projet (par exemple dans les templates)
    path("livres/", liste_livres, name="livres_liste"),
]
