# Generated by Django 4.1 on 2022-08-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status',
            field=models.CharField(choices=[('Aberto', 'Aberto'), ('Em atendimento', 'Em atendimento'), ('Finalizado', 'Finalizado')], max_length=200, null=True),
        ),
    ]
