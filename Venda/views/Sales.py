from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from Venda.models import *
from datetime import date
from Venda.models import *
from Venda.forms import *

# @login_required(login_url = 'Usuario:Login')
def MonthlySales(request):

    datas = []

    data = date.today()

    current_month = data.month
    current_year = data.year

    months = {
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

        list_month.append(months[current_month])

        assistant = Sale.objects.all().filter(month = current_month, year = current_year)

        amount = 0.00

        for aux in assistant:

            amount += aux.netProfit

        datas.append(float(f'{amount:.2f}'))
        
        current_month += 1

        if(current_month > 12):
        
            current_month = 1

            current_year += 1
    
    current_month -= 1

    
    categories = "id", "Produto", 'Unidades', 'Lucro Bruto', 'Tescer', 'Fechar', 'Encher', 'Bordar', 'Linha', 'Caixinha', 'Gasto total', 'Lucro liquido'

    sales = Sale.objects.all().filter(month = current_month, year = current_year)

    sale_value = 0.00
    total_net_profit = 0.00
    weave = 0.00
    close = 0.00
    fill = 0.00
    embroider = 0.00
    line = 0.00
    box = 0.00
    total = 0.00

    for s in sales:

        total_net_profit += s.netProfit
        sale_value += s.grossProfit
        weave += s.spentWeaving
        close += s.spentClose
        fill += s.spentFiling
        embroider += s.spentEmbroider
        line += s.spentLine
        box += s.spentBox
        total += s.totalCost

    context = {
        'title' : 'Vendas do mês',
        'total_net_profit' : f'{total_net_profit:.2f}',
        'sale_value' : f'{sale_value:.2f}',
        'weave' : f'{weave:.2f}',
        'close' : f'{close:.2f}',
        'fill' : f'{fill:.2f}',
        'embroider' : f'{embroider:.2f}',
        'line' : f'{line:.2f}',
        'box' : f'{box:.2f}',
        'total' : f'{total:.2f}',
        'categories' : categories,
        'sales' : sales,
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
        'Sales/MonthlySales.html', 
        context = context,
    )

def General_sales(request):

    form_action = reverse('Sales:General')

    categories = "id", "Produto", 'Unidades', 'Lucro Bruto', 'Tescer', 'Fechar', 'Encher', 'Bordar', 'Linha', 'Caixinha', 'Gasto total', 'Lucro liquido', 'data'

    if request.method == 'POST':

        form = General_Sales_Form(request.POST)

        sales_search = form.save(commit = False)

        sales = Sale.objects.all().filter(month = sales_search.month, year = sales_search.year)

        context = {
            'title' : 'Vendas gerais',
            'sales' : sales,
            'categories' : categories,
            'form' : form,
            'form_action' : form_action,
        }
        
        return render(
            request,
            'Sales/Register.html',
            context = context
        )

    sales = Sale.objects.all()
    
    context = {
        'title' : 'Vendas gerais',
        'sales' : sales,
        'categorias' : categories,
        'form' : General_Sales_Form()
    }

    return render(
        request,
        'Sales/GeneralSales.html',
        context = context
    )