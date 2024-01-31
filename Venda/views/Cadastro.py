from django.shortcuts import render, redirect
from django.urls import reverse
from Venda.models import *
from Venda.forms import *

def CadastroVenda(request):

    form_action = reverse('Vendas:Cadastro-Vendas')

    produtos = Produto.objects.all().filter()

    if request.method == 'POST':

        form = VendaForm(request.POST)

        context = {
            'title' : 'Cadastro Venda',
            'sub_titulo' : 'Cadastro de Venda',
            'produtos' : produtos,
            'form' : form,
            'form_action' : form_action 
        }

        if form.is_valid():

            venda_nova = form.save(commit = False)

            venda_nova.gastoTescer = 0.00

            venda_nova.gastoFechar = 0.00

            venda_nova.gastoEncher = 0.00

            venda_nova.gastoCordao = 0.00

            venda_nova.gastoBordar = 0.00

            venda_nova.gastoLinha = 0.00

            venda_nova.gastoCaixinha = 0.00


            if venda_nova.produto.unidadesSapatinho != 0:

                if venda_nova.produto.genero == True:

                    sapatinho = Produto_Custos_Base.objects.all().filter(Nome = 'sapatinho M')

                else:

                    sapatinho = Produto_Custos_Base.objects.all().filter(Nome = 'sapatinho F')

                sapatinho = sapatinho[0]

                venda_nova.gastoTescer = venda_nova.unidadesVendidas * venda_nova.produto.unidadesSapatinho * sapatinho.Tescer

                venda_nova.gastoFechar = venda_nova.unidadesVendidas * venda_nova.produto.unidadesSapatinho * sapatinho.Fechar

                venda_nova.gastoEncher = venda_nova.unidadesVendidas * venda_nova.produto.unidadesSapatinho * sapatinho.Encher

                venda_nova.gastoCordao = venda_nova.unidadesVendidas * venda_nova.produto.unidadesSapatinho * sapatinho.Cordao

                venda_nova.gastoBordar = venda_nova.unidadesVendidas * venda_nova.produto.unidadesSapatinho * sapatinho.Bordar

                venda_nova.gastoLinha = venda_nova.unidadesVendidas * venda_nova.produto.unidadesSapatinho * sapatinho.Linha

                venda_nova.gastoCaixinha = venda_nova.unidadesVendidas * venda_nova.produto.unidadesSapatinho * sapatinho.Caixinha

            if venda_nova.produto.unidadesLuvinha != 0:

                luvinha = Produto_Custos_Base.objects.get(Nome = 'luvinha')

                venda_nova.gastoTescer += venda_nova.unidadesVendidas * venda_nova.produto.unidadesLuvinha * luvinha.Tescer

                venda_nova.gastoFechar += venda_nova.unidadesVendidas * venda_nova.produto.unidadesLuvinha * luvinha.Fechar

                venda_nova.gastoEncher += venda_nova.unidadesVendidas * venda_nova.produto.unidadesLuvinha * luvinha.Encher

                venda_nova.gastoCordao += venda_nova.unidadesVendidas * venda_nova.produto.unidadesLuvinha * luvinha.Cordao

                venda_nova.gastoBordar += venda_nova.unidadesVendidas * venda_nova.produto.unidadesLuvinha * luvinha.Bordar

                venda_nova.gastoLinha += venda_nova.unidadesVendidas * venda_nova.produto.unidadesLuvinha * luvinha.Linha

                venda_nova.gastoCaixinha = venda_nova.unidadesVendidas * venda_nova.produto.unidadesLuvinha * luvinha.Caixinha

            if venda_nova.produto.unidadesToca != 0:

                touca = Produto_Custos_Base.objects.get(Nome = 'toca')

                print(venda_nova.unidadesVendidas, )

                venda_nova.gastoTescer += venda_nova.unidadesVendidas * venda_nova.produto.unidadesToca * touca.Tescer

                venda_nova.gastoFechar += venda_nova.unidadesVendidas * venda_nova.produto.unidadesToca * touca.Fechar

                venda_nova.gastoEncher += venda_nova.unidadesVendidas * venda_nova.produto.unidadesToca * touca.Encher

                venda_nova.gastoCordao += venda_nova.unidadesVendidas * venda_nova.produto.unidadesToca * touca.Cordao

                venda_nova.gastoBordar += venda_nova.unidadesVendidas * venda_nova.produto.unidadesToca * touca.Bordar

                venda_nova.gastoLinha += venda_nova.unidadesVendidas * venda_nova.produto.unidadesToca * touca.Linha

                venda_nova.gastoCaixinha = venda_nova.unidadesVendidas * venda_nova.produto.unidadesToca * touca.Caixinha

            if venda_nova.produto.unidadesTiara != 0:

                tiara = Produto_Custos_Base.objects.get(Nome = 'tiara')

                venda_nova.gastoTescer += venda_nova.unidadesVendidas * venda_nova.produto.unidadesTiarinha * tiara.Tescer

                venda_nova.gastoFechar += venda_nova.unidadesVendidas * venda_nova.produto.unidadesTiarinha * tiara.Fechar

                venda_nova.gastoEncher += venda_nova.unidadesVendidas * venda_nova.produto.unidadesTiarinha * tiara.Encher

                venda_nova.gastoCordao += venda_nova.unidadesVendidas * venda_nova.produto.unidadesTiarinha * tiara.Cordao

                venda_nova.gastoBordar += venda_nova.unidadesVendidas * venda_nova.produto.unidadesTiarinha * tiara.Bordar

                venda_nova.gastoLinha += venda_nova.unidadesVendidas * venda_nova.produto.unidadesTiarinha * tiara.Linha

                venda_nova.gastoCaixinha = venda_nova.unidadesVendidas * venda_nova.produto.unidadesTiarinha * tiara.Caixinha

            venda_nova.gastoTescer = float(f"{venda_nova.gastoTescer:.2f}")

            venda_nova.gastoFechar = float(f"{venda_nova.gastoFechar:.2f}")

            venda_nova.gastoEncher = float(f"{venda_nova.gastoEncher:.2f}")

            venda_nova.gastoCordao = float(f"{venda_nova.gastoCordao:.2f}")

            venda_nova.gastoBordar = float(f"{venda_nova.gastoBordar:.2f}")

            venda_nova.gastoLinha = float(f"{venda_nova.gastoLinha:.2f}")

            venda_nova.gastoCaixinha = float(f"{venda_nova.gastoCaixinha:.2f}")


            venda_nova.gastoTotal = float(f"{venda_nova.gastoTescer + venda_nova.gastoFechar + venda_nova.gastoEncher + venda_nova.gastoCordao + venda_nova.gastoBordar + venda_nova.gastoLinha + venda_nova.gastoCaixinha:.2f}")

            venda_nova.lucroLiquido = float(f'{venda_nova.lucroBruto - venda_nova.gastoTotal:.2f}')

            venda_nova.save()

            return redirect('Vendas:Menssal')
        
        return render(
            request,
            'Vendas/Cadastro.html',
            context = context
        )
    
    context = {
        'title' : 'Cadastro Venda',
        'sub_titulo' : 'Cadastro de Venda',
        'produtos' : produtos,
        'form' : VendaForm()
    }

    return render(
        request,
        'Vendas/Cadastro.html',
        context = context
    )

def CadastroProduto(request):

    form_action = reverse('Vendas:Cadastro-Produto')

    if request.method == 'POST':

        form = ProdutoForm(request.POST)

        context = {
            'title' : 'Cadastro Venda',
            'sub_titulo' : 'Cadastro de Produto',
            'form' : form,
            'form_action' : form_action 
        }

        if form.is_valid():

            produto_nova = form.save(commit = False)

            produto_nova.save()

            return redirect('Vendas:Menssal')
        
        return render(
            request,
            'Vendas/Cadastro.html',
            context = context
        )
    
    context = {
        'title' : 'Cadastro Venda',
        'sub_titulo' : 'Cadastro de Produto',
        'form' : ProdutoForm()
    }

    return render(
        request,
        'Vendas/Cadastro.html',
        context = context
    )

def CadastroProdutoBase(request):

    form_action = reverse('Vendas:Cadastro-Produto-Base')

    if request.method == 'POST':

        form = CustoBase(request.POST)

        context = {
            'title' : 'Cadastro Venda',
            'sub_titulo' : 'Cadastro de Produto Base',
            'form' : form,
            'form_action' : form_action 
        }

        if form.is_valid():

            produto_nova = form.save(commit = False)

            produto_nova.save()

            return redirect('Vendas:Menssal')
        
        return render(
            request,
            'Vendas/Cadastro.html',
            context = context
        )
    
    context = {
        'title' : 'Cadastro Venda',
        'sub_titulo' : 'Cadastro de Produto Base',
        'form' : CustoBase()
    }

    return render(
        request,
        'Vendas/Cadastro.html',
        context = context
    )