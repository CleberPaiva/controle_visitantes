from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo"
        ]
        error_messages = {
            "nome_completo": {
                "required": "O nome completo do visitante é obrigatório para o registro!"
            },
            "cpf": {
                "required": "O CPF do visitante é obrigatório para o registro!"
            },
            "data_nascimento": {
                "required": "A data de nascimento do visitante é obrigatório para o registro!",
                "invalid": "Por favor, informe um formato válido. (dd/mm/aaaa)"
            },
            "numero_casa": {
                "required": "O número da casa é obrigatório para o registro!"
            }          
        }
        
