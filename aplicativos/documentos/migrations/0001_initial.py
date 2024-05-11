# Generated by Django 5.0.6 on 2024-05-11 00:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pertence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionarios')),
            ],
        ),
    ]