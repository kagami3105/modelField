from django.contrib import admin
from .models import Livre, Auteur

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ("titre", "auteur", "date_publication", "disponible")
    search_fields = ("titre", "isbn", "auteur__nom")
    list_filter = ("disponible", "date_publication")

admin.site.register(Auteur)
