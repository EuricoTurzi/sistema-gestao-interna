# Generated by Django 5.1.1 on 2024-10-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0005_alter_requisicoes_comercial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicoes',
            name='faturamento',
            field=models.CharField(blank=True, choices=[('', ''), ('A Faturar', 'A Faturar'), ('Faturado sem taxa', 'Faturado sem taxa'), ('Faturado com taxa', 'Faturado com taxa'), ('Pendente', 'Pendente'), ('Pendente sem Contrato', 'Pendente sem Contrato'), ('Pendente Sem Termo', 'Pendente Sem Termo'), ('Pendente Sem Contrato', 'Pendente Sem Contrato'), ('Sem Custo', 'Sem Custo'), ('Dados invalidos', 'Dados invalidos')], default='A Faturar', max_length=1200),
        ),
    ]
