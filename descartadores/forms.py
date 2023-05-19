from django import forms
from .models import Descartadores


class DescartadoresForm(forms.ModelForm):
    class Meta:
        model = Descartadores
        fields = ['nome', 'documento', 'email', 'endereco']
