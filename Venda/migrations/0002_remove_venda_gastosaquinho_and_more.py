# Generated by Django 5.0.1 on 2024-01-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='gastoSaquinho',
        ),
        migrations.AlterField(
            model_name='produto_custos_base',
            name='Laco_cordao',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='produto_custos_base',
            name='Tescer',
            field=models.FloatField(),
        ),
    ]