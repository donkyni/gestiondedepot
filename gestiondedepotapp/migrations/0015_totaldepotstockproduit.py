# Generated by Django 3.2 on 2021-08-16 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondedepotapp', '0014_auto_20210809_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalDepotStockProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitedepotstockproduit', models.IntegerField(null=True)),
                ('montantdepotstockproduit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nombrecasierequivalentdepotstockproduit', models.IntegerField(blank=True, help_text='24 bouteilles pour petit model et 12 bouteilles pour grand model', null=True)),
                ('quantiterestantdepotstockproduit', models.IntegerField(blank=True, null=True)),
                ('montantrestantdepotstockproduit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nombrecasierequivalentrestantdepotstockproduit', models.IntegerField(blank=True, help_text='24 bouteilles pour petit model et 12 bouteilles pour grand model', null=True)),
                ('casierperdu', models.IntegerField(default=0, null=True)),
                ('produitperdu', models.IntegerField(default=0, null=True)),
                ('casiercasse', models.IntegerField(default=0, null=True)),
                ('produitcasse', models.IntegerField(default=0, null=True)),
                ('etat', models.BooleanField(default=False, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('datecreationdepotstockproduit', models.DateField(auto_now_add=True, null=True)),
                ('requete_achat', models.DateTimeField(blank=True, null=True)),
                ('datemodificationdepotstockproduit', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatdepotstockproduit', models.BooleanField(default=False, null=True)),
                ('fournisseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.fournisseur')),
                ('parametreprixachatstockproduit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.parametreprixachatstockproduit', verbose_name='Produit prix')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.site')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]