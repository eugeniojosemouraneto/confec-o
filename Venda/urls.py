from django.urls import path
from Venda import views

app_name = 'Vendas'

urlpatterns = [
    path('Vendas/Gerais/', views.VendasGerais, name = 'Gerais'),
    path('Cadastro/Produto-Base/', views.CadastroProdutoBase, name = 'Cadastro-Produto-Base'),
    path('Cadastro/Produto/', views.CadastroProduto, name = 'Cadastro-Produto'),
    path('Cadastro/Venda/', views.CadastroVenda, name = 'Cadastro-Vendas'),
    path('', views.VendasMenssal, name = 'Menssal'),
]
