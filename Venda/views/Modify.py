from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
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

    if product is None:

        raise Http404('Produto não existente')
    
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
            'product' : product,
            'type_page' : 'Produto',
            'form' : form,
            'form_action' : form_action,
        }

        return render(
            request,
            'Sales/Form_Sale_Product.html',
            context = context
        )

    context = {
        'title' : f'Modificar Produto',
        'sub_titulo' : f'Modificar das dados de {product.name}',
        'product' : product,
        'type_page' : 'Produto',
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

    if product_base is None:

        raise Http404('Produto base selecionado não existe')

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
            'product' : product_base,
            'type_page' : 'Produto Base',
            'form' : form,
            'form_action' : form_action,
        }

        return render(
            request,
            'Sales/Form_Sale_Product.html',
            context = context
        )

    context = {
        'title' : f'Modificar Produto Base',
        'sub_titulo' : f'Modificar das dados de {product_base.Name}', 
        'product' : product_base,
        'type_page' : 'Produto Base',
        'url_page' : 'Delete-Product-Base',
        'form' : BaseCost(),
        'form' : BaseCost(instance = product_base),
        'form_action' : form_action,
    }

    return render(
        request,
        'Sales/Form_Sale_Product.html',
        context = context
    )

def Delete_Product(request, id_product, type_page):

    product = None

    if type_page == 'Produto':
        product = get_object_or_404(
            Product,
            pk = id_product
        )
    elif type_page == 'Produto Base':
        product = get_object_or_404(
            Product_Base_Cost,
            pk = id_product
        )

    if product != None:

        product.delete()

    return redirect('Sales:Modify-Menu')