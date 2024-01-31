from Venda.models import *
from django import forms

class VendaForm(forms.ModelForm):

    class Meta:

        model = Venda

        fields = (
            'produto',
            'lucroBruto',
            'unidadesVendidas',
            'dia',
            'mes',
            'ano',
        )
        
        produtos = Produto.objects.all()

class ProdutoForm(forms.ModelForm):

    class Meta:

        model = Produto

        fields = (
            'nome',
            'genero',
            'unidadesSapatinho',
            'unidadesLuvinha',
            'unidadesToca',
            'unidadesTiara'
        )



class VendaFinal(forms.ModelForm):
    
    class Meta:

        model = Venda

        fields = (
            'produto',
            'lucroBruto',
            'unidadesVendidas',
            'gastoTescer',
            'gastoFechar',
            'gastoEncher',
            'gastoCordao',
            'gastoBordar',
            'gastoLinha',
            'gastoCaixinha',
            'gastoTotal',
            'lucroLiquido',
            'dia',
            'mes',
            'ano',
        )
        
        produtos = Produto.objects.all()

        

class CustoBase(forms.ModelForm):

    class Meta:

        model = Produto_Custos_Base

        fields = (
            'Nome',
            'Tescer',
            'Fechar',
            'Encher',
            'Cordao',
            'Bordar',
            'Laco_cordao',
            'Linha',
            'Caixinha'
        )

class Vendas_Gerais_Form(forms.ModelForm):

    class Meta:

        model = Venda

        fields = (
            'mes', 
            'ano',
        )