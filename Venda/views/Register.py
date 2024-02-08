from django.shortcuts import render, redirect
from Venda.constant_variables import *
from django.urls import reverse
from Venda.models import *
from Venda.forms import *

def Register_Sale(request):

    form_action = reverse('Sales:Register-Sales')

    products = Product.objects.all().filter()

    if request.method == 'POST':

        form = SaleForm(request.POST)

        context = {
            'title' : 'Cadastro Venda',
            'sub_titulo' : 'Cadastro de Venda',
            'produtos' : products,
            'form' : form,
            'form_action' : form_action,
        }

        if form.is_valid():

            new_sale = form.save(commit = False)

            new_sale.spentWeaving = new_sale.spentClose = new_sale.spentFiling = new_sale.spentEmbroider = new_sale.spentLine = new_sale.spentBox = 0.00

            if new_sale.product.shoeUnits != 0:

                if new_sale.product.gender == True:

                    slipper = Product_Base_Cost.objects.get(Name = 'sapatinho M')

                else:

                    slipper = Product_Base_Cost.objects.get(Name = 'sapatinho F')

                new_sale.spentWeaving = new_sale.unitsSold * slipper.Weaving

                new_sale.spentClose = new_sale.unitsSold * slipper.Close

                new_sale.spentFiling = new_sale.unitsSold * slipper.Fill

                new_sale.spentEmbroider = new_sale.unitsSold * slipper.Embroider

                new_sale.spentLine = new_sale.unitsSold * slipper.Line

                new_sale.spentBox = new_sale.unitsSold * slipper.Box

            if new_sale.product.gloveUnits != 0:

                glove = Product_Base_Cost.objects.get(Name = 'luvinha')

                new_sale.spentWeaving += new_sale.unitsSold * glove.Weaving

                new_sale.spentClose += new_sale.unitsSold * glove.Close

                new_sale.spentFiling += new_sale.unitsSold * glove.Fill

                new_sale.spentEmbroider += new_sale.unitsSold * glove.Embroider

                new_sale.spentLine += new_sale.unitsSold * glove.Line

                new_sale.spentBox += new_sale.unitsSold * glove.Box

            if new_sale.product.denUnits != 0:

                den = Product_Base_Cost.objects.get(Name = 'toca')

                new_sale.spentWeaving += new_sale.unitsSold * den.Weaving

                new_sale.spentClose += new_sale.unitsSold * den.Close

                new_sale.spentFiling += new_sale.unitsSold * den.Fill

                new_sale.spentEmbroider += new_sale.unitsSold * den.Embroider

                new_sale.spentLine += new_sale.unitsSold * den.Line

                new_sale.spentBox += new_sale.unitsSold * den.Box

            if new_sale.product.tiaraUnits != 0:

                tiara = Product_Base_Cost.objects.get(Name = 'tiara')

                new_sale.spentWeaving += new_sale.unitsSold * tiara.Weaving

                new_sale.spentClose += new_sale.unitsSold * tiara.Close

                new_sale.spentFiling += new_sale.unitsSold * tiara.Fill

                new_sale.spentEmbroider += new_sale.unitsSold * tiara.Embroider

                new_sale.spentLine += new_sale.unitsSold * tiara.Line

                new_sale.spentBox += new_sale.unitsSold * tiara.Box


            new_sale.spentWeaving, new_sale.spentClose, new_sale.spentFiling, new_sale.spentEmbroider, new_sale.spentLine, new_sale.spentBox = format_accurately_list(new_sale.spentWeaving, new_sale.spentClose, new_sale.spentFiling, new_sale.spentEmbroider, new_sale.spentLine, new_sale.spentBox)



            new_sale.totalCost = float(f'{new_sale.spentWeaving + new_sale.spentClose + new_sale.spentFiling + new_sale.spentEmbroider + new_sale.spentLine + new_sale.spentBox:.2f}')

            new_sale.netProfit = float(f'{new_sale.grossProfit - new_sale.totalCost:.2f}')

            new_sale.save()

            return redirect('Sales:Monthly')
        
        return render(
            request,
            'Sales/Form_Sale_Product.html',
            context = context
        )
    
    context = {
        'title' : 'Cadastro Venda',
        'sub_titulo' : 'Cadastro de Venda',
        'produtos' : products,
        'form' : SaleForm(),
    }

    return render(
        request,
        'Sales/Form_Sale_Product.html',
        context = context
    )

def Register_Product(request):

    form_action = reverse('Sales:Register-Product')

    if request.method == 'POST':

        form = ProductForm(request.POST)

        context = {
            'title' : 'Cadastro Venda',
            'sub_titulo' : 'Cadastro de Produto',
            'form' : form,
            'form_action' : form_action 
        }

        if form.is_valid():

            new_product = form.save(commit = False)

            new_product.save()

            return redirect('Sales:Monthly')
        
        return render(
            request,
            'Sales/Form_Sale_Product.html',
            context = context
        )
    
    context = {
        'title' : 'Cadastro Venda',
        'sub_titulo' : 'Cadastro de Produto',
        'form' : ProductForm()
    }

    return render(
        request,
        'Sales/Form_Sale_Product.html',
        context = context
    )

def Product_Registration_Base(request):

    form_action = reverse('Sales:Register-Product-Base')

    if request.method == 'POST':

        form = BaseCost(request.POST)

        context = {
            'title' : 'Cadastro Venda',
            'sub_titulo' : 'Cadastro de Produto Base',
            'form' : form,
            'form_action' : form_action 
        }

        if form.is_valid():

            new_product = form.save(commit = False)

            new_product.save()

            return redirect('Sales:Monthly')
        
        return render(
            request,
            'Sales/Form_Sale_Product.html',
            context = context
        )
    
    context = {
        'title' : 'Cadastro Venda',
        'sub_titulo' : 'Cadastro de Produto Base',
        'form' : BaseCost()
    }

    return render(
        request,
        'Sales/Form_Sale_Product.html',
        context = context
    )