# Generated by Django 5.1.2 on 2024-11-01 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recomendations',
            old_name='Estado',
            new_name='estados',
        ),
    ]
