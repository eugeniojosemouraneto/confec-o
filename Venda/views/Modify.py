from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from Venda.models import *
from Venda.forms import *
from Venda.constant_variables import *

def Modify_Menu(request):

    products = Product.objects.all()

    base_cost = Product_Base_Cost.objects.all()

    context = {
        'title' : 'Alterar',
        'sub_titulo' : 'Menu de alteração',
        'categories_product' : categories_product,
        'products' : products,
        'base_cost' : base_cost,
        'categories_base_cost' : categories_base_cost
    }

    return render(
        request,
        'Sales/Modify_menu.html',
        context = context
    )

def Modify_product(request, id_product):

    product = get_object_or_404(
        Product,
        pk = id_product,
    )

    form_action = reverse('Sales:Modify-Product', args = (id_product,))

    if request.method == 'POST':

        form = ProductForm(request.POST, instance = product)

        if form.is_valid():

            product = form.save(commit = False)

            product.save()

            return redirect('Sales:Modify-Menu')
    
        
        context = {
            'title' : f'Modificar Produto',
            'sub_titulo' : f'Modificar das dados de {product.name}', 
            'form' : form,
            'form_action' : form_action,
        }

        return render(
            request,
            'Sales/Form.html',
            context = context
        )

    context = {
        'title' : f'Modificar Produto',
        'sub_titulo' : f'Modificar das dados de {product.name}', 
        'form' : ProductForm(),
        'form' : ProductForm(instance = product),
        'form_action' : form_action,
    }

    return render(
        request,
        'Sales/Form_Sale_Product.html',
        context = context
    )

def Modify_product_Base(request, id_product_base):

    product_base = get_object_or_404(
        Product_Base_Cost,
        pk = id_product_base,
    )

    form_action = reverse('Sales:Modify-Product-Base', args = (id_product_base,))

    if request.method == 'POST':

        form = BaseCost(request.POST, instance = product_base)

        if form.is_valid():

            product = form.save(commit = False)

            product.save()

            return redirect('Sales:Modify-Menu')
    
        
        context = {
            'title' : f'Modificar Produto Base',
            'sub_titulo' : f'Modificar das dados de {product_base.Name}', 
            'form' : form,
            'form_action' : form_action,
        }

        return render(
            request,
            'Sales/Form.html',
            context = context
        )

    context = {
        'title' : f'Modificar Produto Base',
        'sub_titulo' : f'Modificar das dados de {product_base.Name}', 
        'form' : BaseCost(),
        'form' : BaseCost(instance = product_base),
        'form_action' : form_action,
    }

    return render(
        request,
        'Sales/Form_Sale_Product.html',
        context = context
    )