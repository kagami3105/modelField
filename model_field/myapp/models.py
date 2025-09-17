# myapp/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import uuid

# Définition des choix pour un champ CharField
# C'est une bonne pratique de les définir en dehors de la classe du modèle
PRODUCT_CATEGORIES = (
    ('ELECTRONICS', 'Électronique'),
    ('CLOTHING', 'Vêtements'),
    ('BOOKS', 'Livres'),
    ('FOOD', 'Alimentation'),
)

class Product(models.Model):
    """
    Ce modèle représente un produit dans une boutique en ligne.
    Il utilise une variété de champs pour démontrer les différents types.
    """

    # Champs de base
    # L'AutoField est créé automatiquement par Django comme primary_key par défaut
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="UUID unique pour chaque produit. Non modifiable après la création.",
        verbose_name="ID de l'article"
    )

    # CharField : chaîne de caractères de taille limitée
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=True,
        db_comment="Nom unique du produit.",
        verbose_name="Nom du produit"
    )

    # SlugField : chaîne de caractères pour les URLs, 'slug' = 'limace'
    slug = models.SlugField(
        max_length=250,
        unique=True,
        help_text="Chaîne de caractères pour une URL unique et lisible par l'homme."
    )

    # TextField : champ de texte illimité
    description = models.TextField(
        null=True, # Peut être vide dans la base de données
        blank=True, # Peut être vide dans les formulaires Django
        help_text="Description complète du produit.",
        verbose_name="Description"
    )

    # Choices : utilisation d'une liste de tuples pour des choix prédéfinis
    category = models.CharField(
        max_length=50,
        choices=PRODUCT_CATEGORIES,
        default='ELECTRONICS',
        db_index=True, # Crée un index pour des recherches plus rapides
        help_text="Catégorie du produit.",
        verbose_name="Catégorie"
    )

    # BooleanField : stocke True/False
    is_available = models.BooleanField(
        default=True,
        help_text="Indique si le produit est en stock."
    )

    # IntegerField : entier standard
    stock = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Nombre de produits en stock. Ne peut pas être négatif."
    )

    # DecimalField : pour des valeurs monétaires
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Prix du produit. Max 10 chiffres, 2 décimales."
    )

    # DateField et DateTimeField : pour des dates et heures
    release_date = models.DateField(
        null=True,
        blank=True,
        help_text="Date de sortie du produit."
    )

    created_at = models.DateTimeField(
        auto_now_add=True, # Définit la date et l'heure lors de la création
        help_text="Date et heure de la création du produit."
    )

    updated_at = models.DateTimeField(
        auto_now=True, # Met à jour la date et l'heure à chaque sauvegarde
        help_text="Date et heure de la dernière mise à jour."
    )

    # ImageField : gère les images, nécessite Pillow
    # Exécutez 'pip install Pillow'
    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True,
        help_text="Image du produit."
    )

    # ForeignKey : relation un-à-plusieurs (un vendeur a plusieurs produits)
    # Ici, on utilise 'self' pour une relation récursive
    parent_product = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL, # Définit le champ à NULL si l'objet lié est supprimé
        null=True,
        blank=True,
        related_name='variations', # Permet d'accéder aux variations depuis le parent
        help_text="Produit parent pour les variations de couleur ou de taille."
    )

    class Meta:
        # Attributs de la classe Meta pour des options de modèle
        db_table = 'myproject_products' # Nom de la table dans la base de données
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['name'] # Tri par nom par défaut
        unique_together = ('name', 'category') # S'assure que la combinaison est unique

        # Exemple d'utilisation de unique_for_date
        # unique_for_date='release_date'
        # unique_for_month='release_date'
        # unique_for_year='release_date'
        # Je ne les ajoute pas ici car ils ne sont pas utiles pour ce modèle,
        # mais ils s'utilisent pour s'assurer de l'unicité par période temporelle.

    def __str__(self):
        """Méthode de représentation de l'objet"""
        return self.name