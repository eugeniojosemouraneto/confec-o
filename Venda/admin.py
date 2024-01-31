from django.contrib import admin
from Venda import models

@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = 'nome', 'unidadesSapatinho', 'unidadesLuvinha', 'unidadesToca', 'unidadesTiara', 'genero',

    ordering = 'nome',

    list_per_page = 20

    list_max_show_all = 2000


@admin.register(models.Venda)
class VendaAdmin(admin.ModelAdmin):

    list_display = 'produto', 'lucroBruto', 'unidadesVendidas', 'dia', 'mes', 'ano',

    ordering = 'produto', 'ano',

    list_filter = 'produto', 'mes', 'ano',

    list_per_page = 20

    list_max_show_all = 100000

@admin.register(models.Produto_Custos_Base)
class CustoBase_Adim(admin.ModelAdmin):

    list_display = 'Nome', 'Tescer','Fechar', 'Encher', 'Cordao', 'Bordar', 'Laco_cordao', 'Linha', 'Caixinha'

    list_per_page = 20

    list_max_show_all = 100000

