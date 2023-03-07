from django.db import models
from django.template.defaulttags import register

class NumeroSelecionado(models.Model):
    nome = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    pago= models.BooleanField(default=False)
    selecionado_em = models.DateTimeField(null=True, blank=True)

    def esta_pago(self):
        return NumeroSelecionado.objects.filter(numero=self.numero, pago=True).exists()
    
    def __str__(self):
        return self.nome + ' - ' + self.numero

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome