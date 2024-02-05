from django.urls import path
from Venda import views

app_name = 'Sales'

urlpatterns = [
    path('Consulta/<int:month>/<int:year>/', views.Consultancy_Sales, name = 'Consultancy-Sales'),
    path('Vendas/Gerais/', views.General_sales, name = 'General'),
    path('Cadastro/Produto-Base/', views.Product_Registration_Base, name = 'Register-Product-Base'),
    path('Cadastro/Produto/', views.Register_Product, name = 'Register-Product'),
    path('Cadastro/Venda/', views.Register_Sale, name = 'Register-Sales'),
    path('', views.MonthlySales, name = 'Monthly'),
]
