from Venda.models import *
from django import forms

class SaleForm(forms.ModelForm):

    class Meta:

        model = Sale

        fields = (
            'product',
            'grossProfit',
            'unitsSold',
            'day',
            'month',
            'year',
        )
        
        products = Product.objects.all()

class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = (
            'name',
            'gender',
            'shoeUnits',
            'gloveUnits',
            'denUnits',
            'tiaraUnits'
        )



class VendaFinal(forms.ModelForm):
    
    class Meta:

        model = Sale

        fields = (
            'product',
            'grossProfit',
            'unitsSold',
            'spentWeaving',
            'spentClose',
            'spentFiling',
            'spentEmbroider',
            'spentLine',
            'spentBox',
            'totalCost',
            'netProfit',
            'day',
            'month',
            'year',
        )
        
        products = Product.objects.all()

        

class BaseCost(forms.ModelForm):

    class Meta:

        model = Product_Base_Cost

        fields = (
            'Name',
            'Weaving',
            'Close',
            'Fill',
            'Embroider',
            'Line',
            'Box'
        )

class General_Sales_Form(forms.ModelForm):

    class Meta:

        model = Sale

        fields = (
            'month', 
            'year',
        )