from django.db import models

class Visitantes(models.Model):

    nome_completo = models.CharField(verbose_name="Nome completo", max_length=194)
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    data_nascimento = models.CharField(verbose_name="Da de nascimento", auto_now_add=False, auto_now=False)
    numero_casa = models.PositiveSmallIntegerField(verbose_name="Número da casa visitada")
    placa_veiculo = models.Charfield(verbose_name="Placa veículo", max_length=8, blank=True, null=True)
    horario_chegada = models.DateTimeField(verbose_name="Horário de chegada na portaria", auto_now_add=True)
    horario_saida = models.DateTimeField(verbose_name="Horário de saída", auto_now=False, blank=True, null=True)
    horario_autorizacao = "Horário de autorização"

