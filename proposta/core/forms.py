from django import forms
from proposta.core.models import NumeroSelecionado, Contato

class NumeroSelecionadoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    numero = forms.CharField(max_length=100)

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
