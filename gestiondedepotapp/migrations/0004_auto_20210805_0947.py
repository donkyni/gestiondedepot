# Generated by Django 3.2 on 2021-08-05 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondedepotapp', '0003_venteproduit_no_facture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paniervente',
            name='bb_12',
            field=models.IntegerField(default=0, null=True, verbose_name='Emballage bb de 12 consigné'),
        ),
        migrations.AlterField(
            model_name='paniervente',
            name='bb_24',
            field=models.IntegerField(default=0, null=True, verbose_name='Emballage bb de 24 consigné'),
        ),
        migrations.AlterField(
            model_name='paniervente',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.client', verbose_name='Client régulier'),
        ),
        migrations.AlterField(
            model_name='paniervente',
            name='snb_12',
            field=models.IntegerField(default=0, null=True, verbose_name='Emballage snb de 12 consigné'),
        ),
        migrations.AlterField(
            model_name='paniervente',
            name='snb_24',
            field=models.IntegerField(default=0, null=True, verbose_name='Emballage snb de 24 consigné'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='formatproduit',
            field=models.CharField(choices=[('PM', 'PM'), ('GM', 'GM')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='venteproduit',
            name='bb_12',
            field=models.IntegerField(default=0, null=True, verbose_name='Emballage bb de 12 consigné'),
        ),
        migrations.AlterField(
            model_name='venteproduit',
            name='bb_24',
            field=models.IntegerField(default=0, null=True, verbose_name='Emballage bb de 24 consigné'),
        ),
        migrations.AlterField(
            model_name='venteproduit',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.client', verbose_name='Client régulier'),
        ),
        migrations.AlterField(
            model_name='venteproduit',
            name='snb_12',
            field=models.IntegerField(default=0, null=True, verbose_name='Emballage snb de 12 consigné'),
        ),
        migrations.AlterField(
            model_name='venteproduit',
            name='snb_24',
            field=models.IntegerField(default=0, null=True, verbose_name='Emballage snb de 24 consigné'),
        ),
    ]
