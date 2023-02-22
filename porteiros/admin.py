from django.contrib import admin
from porteiros.models import Porteiro

class PorteiroNome(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'telefone', 'data_nascimento')

admin.site.register(Porteiro, PorteiroNome)
