# Generated by Django 4.1 on 2022-08-23 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0003_chamado_assunto_alter_chamado_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='colaborador',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chamados.colaborador'),
        ),
    ]