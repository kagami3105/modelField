from django.db import models  # Importation du module de modèles de Django
import uuid  # Importation du module uuid pour générer des identifiants uniques


# Modèle représentant un auteur
class Auteur(models.Model):
    """
    Ce modèle est créer pour fournir les informations sur les ouvrages d'un auteur

    """

    # Champ texte pour le nom de l'auteur, limité à 100 caractères
    nom = models.CharField(
        max_length=100,
        verbose_name="Nom de l'auteur",  # C'est pour afficher le nom de l'auteur dans l'interface admin de django
        help_text="Nom complet de l'auteur"  # C'est un texte qui est mis en bas des formulaires pour aider les utilisateurs
    )

    # Champ texte libre pour une biographie, facultatif
    biographie = models.TextField(
        blank=True,  # C'est pour laisser le champ vide
        help_text="Brève biographie"
    )

    # Champ date pour la naissance, facultatif
    date_naissance = models.DateField(
        null=True,  # Permet le stockage d'une valeur nulle dans la base
        blank=True,  # Permet de ne pas remplir le champ dans les formulaires
        help_text="Date de naissance de l’auteur"
    )

    # Champ email, facultatif
    email = models.EmailField(
        blank=True,
        null=True,
        help_text="Email de l’auteur"
    )

    # Méthode spéciale pour afficher l'objet sous forme de chaîne
    def __str__(self):
        return self.nom  # Affiche le nom de l'auteur dans l'admin ou les templates


# Modèle représentant un livre
class Livre(models.Model):
    """
    Ce modèle définit les informations relatives à un livre.
    """

    # Identifiant unique du livre, généré automatiquement avec UUID
    id = models.UUIDField(
        primary_key=True,  # Définit ce champ comme clé primaire
        default=uuid.uuid4,  # Génère un UUID automatiquement
        editable=False,  # Empêche la modification manuelle
        verbose_name="ID unique"
    )

    # Titre du livre, indexé pour des recherches plus rapides
    titre = models.CharField(
        max_length=200,
        db_index=True,  # Crée un index en base de données
        verbose_name="Titre du livre",
        help_text="Titre officiel du livre"
    )

    # Slug unique pour une URL propre (ex: "les misérables de Victor HUGO")
    slug = models.SlugField(
        unique=True,
        help_text="Version url-friendly du titre"
    )

    # Description ou résumé du livre, facultatif
    description = models.TextField(
        blank=True,
        help_text="Résumé ou description"
    )

    # Date de publication, facultative
    date_publication = models.DateField(
        null=True,
        blank=True,
        help_text="Date de publication"
    )

    # Image de couverture, stockée dans le dossier "couvertures/"
    couverture = models.ImageField(
        upload_to="couvertures/",
        blank=True,
        null=True,
        help_text="Image de couverture"
    )

    # Indique si le livre est disponible pour le prêt
    disponible = models.BooleanField(
        default=True,
        help_text="Disponibilité pour le prêt"
    )

    # Prix du livre en euros, avec 2 décimales
    prix = models.DecimalField(
        max_digits=7,  # Jusqu'à 7 chiffres maximum
        decimal_places=2,
        default=0.0,
        help_text="Prix d'achat en €"
    )

    # Lien vers l'auteur principal du livre
    auteur = models.ForeignKey(
        Auteur,
        on_delete=models.CASCADE,  # Supprime le livre si l'auteur est supprimé
        related_name="livres",  # Permet d'accéder aux livres via auteur.livres
        verbose_name="Auteur principal"
    )

    # Liste des co-auteurs, relation multiple
    co_auteurs = models.ManyToManyField(
        Auteur,
        related_name="livres_coauteur",  # Permet d'accéder aux livres via auteur.livres_coauteur
        blank=True,
        verbose_name="Co-auteurs"
    )

    # Code ISBN unique du livre
    isbn = models.CharField(
        max_length=20,
        unique=True,
        help_text="Code ISBN du livre"
    )

    # Fichier PDF du livre, stocké dans "livres/pdf/"
    fichier_pdf = models.FileField(
        upload_to="livres/pdf/",
        blank=True,
        null=True,
        help_text="Version PDF du livre"
    )

    # Méthode spéciale pour afficher le livre sous forme de chaîne
    def __str__(self):
        return self.titre  # Affiche le titre dans l'admin ou les templates