from django.contrib import admin
from .models import NumeroSelecionado, Contato

class NumeroSelecionadoAdmin(admin.ModelAdmin):
    list_display = ['nome','numero','pago']
    list_editable = ['pago']
    pass

class contatoAdmin(admin.ModelAdmin):
    pass

admin.site.register(NumeroSelecionado, NumeroSelecionadoAdmin)
admin.site.register(Contato, contatoAdmin)
