# Generated by Django 3.2 on 2021-08-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondedepotapp', '0008_auto_20210809_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paniervente',
            name='no_facture',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Libelle de facture'),
        ),
        migrations.AlterField(
            model_name='venteproduit',
            name='no_facture',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Libelle de facture'),
        ),
    ]
