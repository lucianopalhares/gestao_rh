# Generated by Django 5.0.6 on 2024-05-10 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departamentos',
            old_name='nome',
            new_name='name',
        ),
    ]
