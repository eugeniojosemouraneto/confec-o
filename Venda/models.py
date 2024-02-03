from django.db import models
from django.contrib.auth.models import User

class Produto_Custos_Base(models.Model):

    class Meta:

        verbose_name = 'Produto_base'

        verbose_name_plural = 'Produtos_bases'

    Nome = models.CharField(max_length = 100)

    Tescer = models.FloatField()

    Fechar = models.FloatField()

    Encher = models.FloatField()

    Cordao = models.FloatField()

    Bordar = models.FloatField()

    Laco_cordao = models.FloatField()

    Linha = models.FloatField()

    Caixinha = models.FloatField(default = 0.00)

    def __str__(self) -> str:
        
        return f'{self.Nome}'
    

class Produto(models.Model):

    class Meta:

        verbose_name = 'Produto'

        verbose_name_plural = 'Produtos'

    nome = models.CharField(max_length = 100, default = "")

    genero = models.BooleanField(default = 0)

    unidadesSapatinho = models.IntegerField(default = 0)

    unidadesLuvinha = models.IntegerField(default = 0)

    unidadesToca = models.IntegerField(default = 0)

    unidadesTiara = models.IntegerField(default = 0)

    def __str__(self) -> str:
        
        return f'{self.nome}'

class Venda(models.Model):

    class Meta:

        verbose_name = 'Venda'

        verbose_name_plural = 'Vendas'

    produto = models.ForeignKey(
        Produto, 
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    lucroBruto = models.FloatField(
        blank = True,
        null = True
    )

    unidadesVendidas = models.IntegerField()

    gastoTescer = models.FloatField()

    gastoFechar = models.FloatField()

    gastoEncher = models.FloatField()

    gastoCordao = models.FloatField()

    gastoBordar = models.FloatField()

    gastoLinha = models.FloatField()

    gastoCaixinha = models.FloatField(default = 0.00)

    gastoTotal = models.FloatField()

    lucroLiquido = models.FloatField()

    dia = models.IntegerField()

    mes = models.IntegerField()

    ano = models.IntegerField()

    def __str__(self) -> str:
        
        return f'{self.produto}'
    
    def __str__(self) -> int:

        return f'{self.mes}'
    
class RelatorioMenssal(models.Model):

    class Meta:

        verbose_name = 'Relatorio_menssal'

        verbose_name_plural = 'Relatorios_menssais'

    mes = models.IntegerField()

    ano = models.IntegerField()

    valorTotal = models.FloatField()
