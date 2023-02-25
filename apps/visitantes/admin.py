from django.contrib import admin
from visitantes.models import Visitante

class VisitanteLista(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf')

admin.site.register(Visitante, VisitanteLista)