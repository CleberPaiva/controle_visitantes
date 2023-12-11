from django.shortcuts import render
from visitantes.models import Visitante

def index(request):
    usuario_logado = request.user  # Acessa o usuário logado
    print(usuario_logado.email)

    if usuario_logado.is_authenticated:
        # Supondo que o usuário logado tenha um campo 'nome_empresa'
        nome_empresa_usuario_logado = usuario_logado.nome_empresa
        print(nome_empresa_usuario_logado)

        # Filtrar visitantes pelo 'numero_casa' que corresponde ao 'nome_empresa' do usuário logado
        todos_visitantes = Visitante.objects.filter(numero_casa=nome_empresa_usuario_logado)
        print(todos_visitantes)
    else:
        # Se nenhum usuário estiver logado, não retorna visitantes
        todos_visitantes = Visitante.objects.none()
        print(todos_visitantes)

    context = {
        "nome_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes,
    }

    return render(request, "index.html", context)
