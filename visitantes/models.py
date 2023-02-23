from django.db import models

class Visitante(models.Model):

    nome_completo = models.CharField(
        verbose_name="Nome completo", 
        max_length=194
        )

    cpf = models.CharField(
        verbose_name="CPF", 
        max_length=11
        )

    data_nascimento = models.DateField(
        verbose_name="Da de nascimento", 
        auto_now_add=False, 
        auto_now=False
        )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Número da casa visitada"
        )

    placa_veiculo = models.CharField(
        verbose_name="Placa veículo", 
        max_length=8, 
        blank=True, 
        null=True
        )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada na portaria", 
        auto_now_add=True
        )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída", 
        auto_now=False, 
        blank=True, 
        null=True
        )

    horario_autorizacao = models.DateTimeField(
        verbose_name= "Horário de autorização",
        auto_now=False, 
        blank=True, 
        null=False
        )

    morador_responsavel = models.CharField(
        verbose_name="Morador responsável pela autorização", 
        max_length=194, 
        blank=True
        )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável",
        on_delete=models.PROTECT
    )    

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def _str_(self):
        return self.nome_completo

