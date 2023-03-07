# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from proposta.core.models import NumeroSelecionado, Contato
from  proposta.core.forms import ContatoForm, NumeroSelecionadoForm
from  proposta.core.models import Contato
from django.contrib import messages
from datetime import datetime, timedelta

def matriz(request):

    if request.method == 'POST':
        form = NumeroSelecionadoForm(request.POST)
    
        if form.is_valid():
            nome = form.cleaned_data['nome']
            numeros = form.cleaned_data['numero'].split(',')
            for num in numeros:
                num = num.strip() # Remove espaços em branco no início e no final do número
                # Verifica se o número já foi selecionado por outra pessoa
                if NumeroSelecionado.objects.filter(numero=num, pago=True).exists():
                    messages.error(request, f"O número {num} já foi selecionado por outra pessoa.")
                else:
                    # Cria uma nova instância do modelo NumeroSelecionado e salva no banco de dados
                    novo_numero = NumeroSelecionado(nome=nome, numero=num, pago=False)
                    novo_numero.save()
                    messages.success(request, f"Número {num} selecionado com sucesso!")
        else:
            messages.error(request, "Por favor, preencha todos os campos do formulário.")

        # Redireciona o usuário para a página principal
        return redirect('matriz')

    else:
        form = NumeroSelecionadoForm()
        
    selecionados = NumeroSelecionado.objects.order_by('numero')   
    numeros_pagos = NumeroSelecionado.objects.filter(pago=True).values_list('numero', flat=True)
    numeros_disponiveis = NumeroSelecionado.objects.filter(pago=False).values_list('numero', flat=True)
    
        # Calcule o limite de tempo para marcar números não selecionados como amarelos
    contador = datetime.now() - timedelta(hours=24)
    
    numeros = []
    for i in range(1, 101):
        numero = {'numero': i, 'pago': False, 'pendente': False}
        if NumeroSelecionado.objects.filter(numero=i, pago=True).exists():
            numero['pago'] = True
        elif  NumeroSelecionado.objects.filter(numero=i, pago=False).exists():
            numero['pendente'] = True
        numeros.append(numero)

    context = {
            'form': form,
            'numeros': numeros,
            'selecionados': selecionados,
            'numeros_disponiveis': numeros_disponiveis,
            'numeros_pagos': numeros_pagos,
            }
    return render(request, 'matriz.html', context)

def proxima_pagina(request):
    
    if request.method == 'POST':
        form = NumeroSelecionadoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            contato = Contato(nome=nome, email=email, mensagem=mensagem)
            contato.save()
            return redirect('matriz')
        
        
    if request.method == 'GET':
        nome = request.GET.get('name', '')
        numeros_selecionados_str = request.GET.get('numeros', '')
        numeros_selecionados = [int(n) for n in numeros_selecionados_str.split(',') if n]

        for num in numeros_selecionados:
            numero_selecionado = NumeroSelecionado(numero=num, autorizado=True, selecionado_por=nome)
            numero_selecionado.save()

        return render(request, 'proxima_pagina.html', {'nome': nome,
                                                       'numeros_selecionados': numeros_selecionados})

    return render(request, 'proxima_pagina.html')


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            contato = Contato(nome=nome, email=email, mensagem=mensagem)
            contato.save()
            return redirect('matriz')
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form})