from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Product_Base_Cost(models.Model):

    class Meta:

        verbose_name = 'Produto_base'

        verbose_name_plural = 'Produtos_bases'

    Name = models.CharField(max_length = 100)

    Weaving = models.FloatField()

    Close = models.FloatField()

    Fill = models.FloatField()

    Embroider = models.FloatField()

    Line = models.FloatField()

    Box = models.FloatField(default = 0.00)

    def __str__(self) -> str:
        
        return f'{self.Name}'
    

class Product(models.Model):

    class Meta:

        verbose_name = 'Produto'

        verbose_name_plural = 'Produtos'

    name = models.CharField(max_length = 100, default = "")

    gender = models.BooleanField(default = 0)

    shoeUnits = models.IntegerField(default = 0)

    gloveUnits = models.IntegerField(default = 0)

    denUnits = models.IntegerField(default = 0)

    tiaraUnits = models.IntegerField(default = 0)

    def __str__(self) -> str:
        
        return f'{self.name}'

class Sale(models.Model):

    class Meta:

        verbose_name = 'Venda'

        verbose_name_plural = 'Vendas'

    product = models.ForeignKey(
        Product, 
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    grossProfit = models.FloatField(
        blank = True,
        null = True
    )

    unitsSold = models.IntegerField()

    spentWeaving = models.FloatField()

    spentClose = models.FloatField()

    spentFiling = models.FloatField()

    spentEmbroider = models.FloatField()

    spentLine = models.FloatField()

    spentBox = models.FloatField()

    totalCost = models.FloatField()

    netProfit = models.FloatField()

    day = models.IntegerField(default = date.today().day)

    month = models.IntegerField(default = date.today().month)

    year = models.IntegerField(default = date.today().year)

    def __str__(self) -> str:
        
        return f'{self.product}'
