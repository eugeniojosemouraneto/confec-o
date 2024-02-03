from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from Venda.models import *
from datetime import date
from Venda.models import *
from Venda.forms import *
from random import randrange

# @login_required(login_url = 'Usuario:Login')
def VendasMenssal(request):

    datas = []

    data = date.today()

    current_month = data.month
    current_year = data.year

    meses = {
        1 : 'Jan',
        2 : 'Fev',
        3 : 'Mar',
        4 : 'Abr',
        5 : 'Mai',
        6 : 'Jun',
        7 : 'Jul',
        8 : 'Ago',
        9 : 'Out',
        10 : 'Set',
        11 : 'Nov',
        12 : 'Dez'
    }

    list_month = []

    for i in range(6):
        
        current_month -=1

        if(current_month <= 0):
        
            current_month = 12

            current_year -= 1
        
    current_month += 1

    for i in range(6):

        list_month.append(meses[current_month])

        assistant = Venda.objects.all().filter(mes = current_month, ano = current_year)

        amount = 0.00

        for aux in assistant:

            amount += aux.lucroLiquido

        datas.append(float(f'{amount:.2f}'));

        print(list_month[i], datas[i])
        
        current_month += 1

        if(current_month > 12):
        
            current_month = 1

            current_year += 1
    
    current_month -= 1

    
    categorias = "id", "Produto", 'Unidades', 'Lucro Bruto', 'Tescer', 'Fechar', 'Encher', 'Bordar', 'Linha', 'Caixinha', 'Gasto total', 'Lucro liquido'

    vendas = Venda.objects.all().filter(mes = current_month, ano = current_year)

    valor_venda = 0.00
    lucro_liquido_total = 0.00
    tescer = 0.00
    fechar = 0.00
    encher = 0.00
    bordar = 0.00
    linha = 0.00
    caixinha = 0.00
    total = 0.00

    for ven in vendas:

        lucro_liquido_total += ven.lucroLiquido
        valor_venda += ven.lucroBruto
        tescer += ven.gastoTescer
        fechar += ven.gastoFechar
        encher += ven.gastoEncher
        bordar += ven.gastoBordar
        linha += ven.gastoLinha
        caixinha += ven.gastoCaixinha
        total += ven.gastoTotal

    context = {
        'title' : 'Vendas do mês',
        'lucro_liquido_total' : f'{lucro_liquido_total:.2f}',
        'valor_venda' : f'{valor_venda:.2f}',
        'tescer' : f'{tescer:.2f}',
        'fechar' : f'{fechar:.2f}',
        'encher' : f'{encher:.2f}',
        'bordar' : f'{bordar:.2f}',
        'linha' : f'{linha:.2f}',
        'caixinha' : f'{caixinha:.2f}',
        'total' : f'{total:.2f}',
        'categoria' : categorias,
        'vendas' : vendas,
        'month1' : list_month[0],
        'month2' : list_month[1],
        'month3' : list_month[2],
        'month4' : list_month[3],
        'month5' : list_month[4],
        'month6' : list_month[5],
        'data_month1' : datas[0],
        'data_month2' : datas[1],
        'data_month3' : datas[2],
        'data_month4' : datas[3],
        'data_month5' : datas[4],
        'data_month6' : datas[5],
    }

    return render(
        request,
        'Vendas/VendaMenssal.html', 
        context = context,
    )

def VendasGerais(request):

    form_action = reverse('Vendas:Gerais')

    categorias = "id", "Produto", 'Unidades', 'Lucro Bruto', 'Tescer', 'Fechar', 'Encher', 'Bordar', 'Linha', 'Caixinha', 'Gasto total', 'Lucro liquido', 'data'

    if request.method == 'POST':

        form = Vendas_Gerais_Form(request.POST)

        busca_vendas = form.save(commit = False)

        vendas = Venda.objects.all().filter(mes = busca_vendas.mes, ano = busca_vendas.ano)

        context = {
            'title' : 'Vendas gerais',
            'Vendas' : vendas,
            'categorias' : categorias,
            'form' : form,
            'form_action' : form_action,
        }
        
        return render(
            request,
            'Vendas/Cadastro.html',
            context = context
        )

    vendas = Venda.objects.all()
    
    context = {
        'title' : 'Vendas gerais',
        'vendas' : vendas,
        'categorias' : categorias,
        'form' : Vendas_Gerais_Form()
    }

    return render(
        request,
        'Vendas/VendasGerais.html',
        context = context
    )