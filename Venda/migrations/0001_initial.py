# Generated by Django 5.0.1 on 2024-01-26 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=100)),
                ('genero', models.BooleanField(default=0)),
                ('unidadesSapatinho', models.IntegerField(default=0)),
                ('unidadesLuvinha', models.IntegerField(default=0)),
                ('unidadesToca', models.IntegerField(default=0)),
                ('unidadesTiara', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Produto_Custos_Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Tescer', models.FloatField(default=0.0)),
                ('Fechar', models.FloatField()),
                ('Encher', models.FloatField()),
                ('Cordao', models.FloatField()),
                ('Bordar', models.FloatField()),
                ('Laco_cordao', models.FloatField(default=0.0)),
                ('Linha', models.FloatField()),
            ],
            options={
                'verbose_name': 'Produto_base',
                'verbose_name_plural': 'Produtos_bases',
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lucroBruto', models.FloatField(blank=True, null=True)),
                ('unidadesVendidas', models.IntegerField()),
                ('gastoTescer', models.FloatField()),
                ('gastoFechar', models.FloatField()),
                ('gastoEncher', models.FloatField()),
                ('gastoSaquinho', models.FloatField()),
                ('gastoCordao', models.FloatField()),
                ('gastoBordar', models.FloatField()),
                ('gastoLinha', models.FloatField()),
                ('gastoTotal', models.FloatField()),
                ('lucroLiquido', models.FloatField()),
                ('dia', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Venda.produto')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]
