from django import forms
from .models import Descartes


class DescartesForm(forms.ModelForm):
    class Meta:
        model = Descartes
        fields = ['nome', 'tipo', 'quantidade', 'descartador', 'ecoponto']
