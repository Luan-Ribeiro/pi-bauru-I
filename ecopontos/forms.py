from django import forms
from .models import Ecopontos


class EcopontosForm(forms.ModelForm):
    class Meta:
        model = Ecopontos
        fields = ['cep', 'bairro', 'endereco', 'situacao']
