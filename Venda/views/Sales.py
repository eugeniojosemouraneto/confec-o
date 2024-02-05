from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Venda.constant_variables import *
from django.urls import reverse
from Venda.models import *
from Venda.forms import *

# @login_required(login_url = 'Usuario:Login')
def MonthlySales(request):

    list_month = []
    datas = []

    list_month, profit, expense = profit_expense_six_months(current_month, current_year) # variables in the constant_variables file
    
    sales = Sale.objects.all().filter(month = current_month, year = current_year) # variables in the constant_variables file

    total_net_profit, sale_value, weave, close, fill, embroider, line, box, total = table_values(sales)

    context = {
        'title' : 'Vendas do mês',
        'total_net_profit' : total_net_profit,
        'sale_value' : sale_value,
        'weave' : weave,
        'close' : close,
        'fill' : fill,
        'embroider' : embroider,
        'line' : line,
        'box' : box,
        'total' : total,
        'categories' : categories, # variables in the constant_variables file
        'sales' : sales,
        'month1' : list_month[0],             # variables in the constant_variables file
        'month2' : list_month[1],             #             *****
        'month3' : list_month[2],             #             *****
        'month4' : list_month[3],             #             *****
        'month5' : list_month[4],             #             *****
        'month6' : list_month[5],             #             *****
        'monthly_profit_data1' : profit[0],   #             *****
        'monthly_profit_data2' : profit[1],   #             *****
        'monthly_profit_data3' : profit[2],   #             *****
        'monthly_profit_data4' : profit[3],   #             *****
        'monthly_profit_data5' : profit[4],   #             *****
        'monthly_profit_data6' : profit[5],   #             *****
        'monthly_expense_data1' : expense[0], #             *****
        'monthly_expense_data2' : expense[1], #             *****
        'monthly_expense_data3' : expense[2], #             *****
        'monthly_expense_data4' : expense[3], #             *****
        'monthly_expense_data5' : expense[4], #             *****
        'monthly_expense_data6' : expense[5], # variables in the constant_variables file
        'status_charts' : True
    }

    return render(
        request,
        'Sales/MonthlySales.html', 
        context = context,
    )

def General_sales(request):

    form_action = reverse('Sales:General')

    if request.method == 'POST':

        form = General_Sales_Form(request.POST)

        informt = form.save(commit = False)

        sales = Sale.objects.all().filter(month = informt.month, year = informt.year)

        return redirect('Sales:Consultancy-Sales', month = informt.month, year = informt.year)

    sales = Sale.objects.all()

    context = {
        'title' : 'Vendas gerais',
        'sales' : sales,
        'categorias' : categories, # variables in the constant_variables file
        'form' : General_Sales_Form(),
    }

    return render(
        request,
        'Sales/GeneralSales.html',
        context = context
    )

def Consultancy_Sales(request, month, year):

    sales = Sale.objects.all().filter(month = month, year = year)

    total_net_profit, sale_value, weave, close, fill, embroider, line, box, total = table_values(sales)

    context = {
        'title' : 'Vendas do mês',
        'total_net_profit' : total_net_profit,
        'sale_value' : sale_value,
        'weave' : weave,
        'close' : close,
        'fill' : fill,
        'embroider' : embroider,
        'line' : line,
        'box' : box,
        'total' : total,
        'categories' : categories, # variables in the constant_variables file
        'sales' : sales,
        'status_charts' : False

        
    }

    return render(
        request,
        'Sales/MonthlySales.html', 
        context = context,
    )