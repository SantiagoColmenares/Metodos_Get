# Generated by Django 5.0.2 on 2024-03-16 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='nombreE',
            new_name='nombre',
        ),
    ]
