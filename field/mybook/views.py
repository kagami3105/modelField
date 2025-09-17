# Importation de la fonction 'render' qui permet de générer une réponse HTTP avec un template HTML
from django.shortcuts import render

# Importation du modèle 'Livre' depuis le fichier models.py du même répertoire
from .models import Livre

# Définition d'une vue appelée 'liste_livres' qui sera appelée lorsqu'un utilisateur accède à une certaine URL
def liste_livres(request):
    # Récupération de tous les objets 'Livre' depuis la base de données
    livres = Livre.objects.all()
    
    # Génération d'une réponse HTTP en rendant le template 'livres_liste.html'
    # On passe les livres récupérés au template via le contexte {'livres': livres}
    return render(request, "mybook/livres_liste.html", {"livres": livres})