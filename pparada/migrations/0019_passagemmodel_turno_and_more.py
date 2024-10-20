# Generated by Django 5.1.1 on 2024-10-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0018_passagemmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='passagemmodel',
            name='turno',
            field=models.CharField(blank=True, choices=[('Dia', 'Dia'), ('Noite', 'Noite')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='passagemmodel',
            name='nome_do_posto',
            field=models.CharField(blank=True, choices=[('POSTO DA SERRA', 'POSTO DA SERRA'), ('POSTO BURITIZINHO', 'POSTO BURITIZINHO'), ('POSTO BRASILEIRÃO', 'POSTO BRASILEIRÃO'), ('POSTO TREVÃO', 'POSTO TREVÃO'), ('POSTO JN', 'POSTO JN'), ('POSTO CAPIXABOM', 'POSTO CAPIXABOM'), ('POSTO GRAAL RUBI', 'POSTO GRAAL RUBI')], max_length=255, null=True),
        ),
    ]
