# Generated by Django 4.2.1 on 2023-05-16 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('descartes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='descartes',
            old_name='documento',
            new_name='descartador',
        ),
    ]