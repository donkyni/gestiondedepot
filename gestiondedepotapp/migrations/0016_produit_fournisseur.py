# Generated by Django 3.2.9 on 2022-03-18 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondedepotapp', '0015_totaldepotstockproduit'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.fournisseur'),
        ),
    ]
