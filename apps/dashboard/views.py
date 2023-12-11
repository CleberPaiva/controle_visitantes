from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from visitantes.models import Visitante
from django.utils import timezone

@login_required
def index(request):
    usuario_logado = request.user  # Acessa o usuário logado
    print(usuario_logado.email)

    if usuario_logado.is_authenticated:
        # Supondo que o usuário logado tenha um campo 'nome_empresa'
        nome_empresa_usuario_logado = usuario_logado.nome_empresa

        # Filtrar visitantes pelo 'numero_casa' que corresponde ao 'nome_empresa' do usuário logado
        todos_visitantes = Visitante.objects.filter(numero_casa=nome_empresa_usuario_logado)
    else:
        # Se nenhum usuário estiver logado, não retorna visitantes
        todos_visitantes = Visitante.objects.none()

    visitantes_aguardando = todos_visitantes.filter(status="AGUARDANDO")
    visitantes_em_visita = todos_visitantes.filter(status="EM_VISITA")
    visitantes_finalizado = todos_visitantes.filter(status="FINALIZADO")

    hora_atual = timezone.now()
    mes_atual = hora_atual.month
    visitantes_mes = todos_visitantes.filter(horario_chegada__month=mes_atual)

    context = {
        "nome_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizado": visitantes_finalizado.count(),
        "visitantes_mes": visitantes_mes.count(),
    }

    return render(request, "index.html", context)
