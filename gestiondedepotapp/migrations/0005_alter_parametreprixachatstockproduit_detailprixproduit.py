# Generated by Django 3.2 on 2021-08-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondedepotapp', '0004_auto_20210805_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametreprixachatstockproduit',
            name='detailprixproduit',
            field=models.CharField(choices=[('Casier entier', 'Casier entier'), ('Trois-quart de casier', 'Trois-quart de casier'), ('Démi-casier', 'Démi-asier '), ('Quart de casier', 'Quart de casier')], max_length=25, null=True),
        ),
    ]
