from django.contrib import admin
from Venda import models

@admin.register(models.Product)
class Product_Admin(admin.ModelAdmin):

    list_display = 'name', 'shoeUnits', 'gloveUnits', 'denUnits', 'denUnits', 'gender',

    ordering = 'name',

    list_per_page = 20

    list_max_show_all = 2000


@admin.register(models.Sale)
class Sale_Admin(admin.ModelAdmin):

    list_display = 'product', 'grossProfit', 'unitsSold', 'day', 'month', 'year',

    ordering = 'product', 'year', 'month'

    list_filter = 'product', 'month', 'year',

    list_per_page = 20

    list_max_show_all = 100000

@admin.register(models.Product_Base_Cost)
class Cost_Basis_Adim(admin.ModelAdmin):

    list_display = 'Name', 'Weaving','Close', 'Fill', 'Embroider', 'Line', 'Box'

    list_per_page = 20

    list_max_show_all = 100000

