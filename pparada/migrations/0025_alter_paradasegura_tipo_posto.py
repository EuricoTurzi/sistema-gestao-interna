# Generated by Django 5.1.1 on 2024-10-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0024_alter_passagemmodel_nome_do_posto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paradasegura',
            name='tipo_posto',
            field=models.CharField(blank=True, choices=[('---', '---'), ('1', 'POSTO DA SERRA'), ('2', 'POSTO BURITIZINHO'), ('3', 'POSTO BRASILEIRÃO'), ('4', 'POSTO TREVÃO'), ('5', 'POSTO JN'), ('6', 'POSTO CAPIXABOM'), ('7', 'POSTO GRAAL RUBI')], default='1', max_length=255, null=True),
        ),
    ]
