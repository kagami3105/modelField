# myapp/admin.py

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Personnalisation de l'affichage du modèle Product dans l'interface d'administration.
    """
    # Affiche ces champs dans la liste du tableau
    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'is_available',
        'created_at'
    )

    # Permet de filtrer les résultats
    list_filter = ('is_available', 'category')

    # Ajoute une barre de recherche
    search_fields = ('name', 'description')

    # Pré-remplit le slug à partir du nom
    prepopulated_fields = {'slug': ('name',)}

    # Rend les champs en lecture seule
    readonly_fields = ('id', 'created_at', 'updated_at')

    # Sépare les champs en sections pour une meilleure organisation
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'category', 'image')
        }),
        ('Informations de stock et de prix', {
            'fields': ('price', 'stock', 'is_available')
        }),
        ('Relation', {
            'fields': ('parent_product',)
        }),
        ('Dates', {
            'fields': ('release_date', 'created_at', 'updated_at'),
            'classes': ('collapse',) # Rend la section repliable
        }),
    )