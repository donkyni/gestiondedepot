# Generated by Django 3.2 on 2021-08-09 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondedepotapp', '0006_paramprixproduitvente_detailprixvente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paramprixproduitvente',
            name='libelle',
        ),
    ]