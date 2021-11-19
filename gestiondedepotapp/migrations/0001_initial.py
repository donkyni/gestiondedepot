# Generated by Django 3.2 on 2021-08-01 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('pseudo', models.CharField(help_text="Le nom d'utilisateur servira à se connecter à la plateforme", max_length=255, null=True, unique=True)),
                ('nom', models.CharField(max_length=255, null=True)),
                ('prenom', models.CharField(max_length=255, null=True)),
                ('adresse', models.CharField(max_length=255, null=True)),
                ('telephone', models.BigIntegerField(null=True, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('sexe', models.CharField(blank=True, choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=120, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_d_ajout', models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date d'enrégistrement de l'utilisateur")),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'verbose_name_plural': 'Utilisateur',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='CategorieProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libellecategorieproduit', models.CharField(max_length=100, null=True, verbose_name='Catégorie')),
                ('datecreationcategorieproduit', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationcategorieproduit', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatcategorieproduit', models.BooleanField(default=False, null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelleclient', models.CharField(max_length=100, null=True)),
                ('adresse', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('datecreation', models.DateField(auto_now_add=True, null=True)),
                ('datemodification', models.DateField(auto_now_add=True, null=True)),
                ('etat', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bb_12', models.IntegerField(blank=True, help_text="Entrer le nombre total de casier de 12 BB emporter pour l'achat", null=True, verbose_name="Total casier de 12 BB empoter pour l'achat")),
                ('bb_24', models.IntegerField(blank=True, help_text="Entrer le nombre total de casier de 24 BB emporter pour l'achat", null=True, verbose_name="Total casier de 24 BB empoter pour l'achat")),
                ('snb_12', models.IntegerField(blank=True, help_text="Entrer le nombre total de casier de 12 SNB emporter pour l'achat", null=True, verbose_name="Total casier de 12 SNB empoter pour l'achat")),
                ('snb_24', models.IntegerField(blank=True, help_text="Entrer le nombre total de casier de 24 SNB emporter pour l'achat", null=True, verbose_name="Total casier de 24 SNB empoter pour l'achat")),
                ('etat', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DepotStockProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_facture', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de facture')),
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
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Droits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_du_droit', models.CharField(max_length=255)),
                ('archive', models.BooleanField(default=False, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Droits',
                'verbose_name_plural': 'Droits',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='DroitsProfils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecriture', models.BooleanField(default=False, null=True)),
                ('lecture', models.BooleanField(default=False, null=True)),
                ('modification', models.BooleanField(default=False, null=True)),
                ('suppression', models.BooleanField(default=False, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('droit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.droits')),
            ],
            options={
                'verbose_name': 'Droits profils',
                'verbose_name_plural': 'Droits profils',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Emballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelleemballage', models.CharField(max_length=255, null=True, verbose_name="Libelle de l'emballage")),
                ('format', models.CharField(choices=[('12', '12'), ('24', '24')], max_length=7, null=True)),
                ('type', models.CharField(choices=[('SNB', 'SNB'), ('BB', 'BB')], max_length=8, null=True)),
                ('datecreationemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatemballage', models.BooleanField(default=False, null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libellefournisseur', models.CharField(blank=True, max_length=100, null=True)),
                ('adressefournisseur', models.CharField(max_length=100, null=True)),
                ('telephonefournisseur', models.CharField(max_length=25, null=True)),
                ('datecreationfournisseur', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationfournisseur', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatfournisseur', models.BooleanField(default=False, null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='HistoriquesDesAchats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_facture', models.CharField(max_length=15, null=True)),
                ('date_achat', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParametrePrixEmballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prixparametreprixemballage', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('datecreationparametreprixemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationparametreprixemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatparametreprixemballage', models.BooleanField(default=False, null=True)),
                ('emballage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.emballage')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ParamPrixProduitVente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=100, null=True)),
                ('prixreelle', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('prixarrondi', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('remise', models.IntegerField(blank=True, null=True)),
                ('datecreation', models.DateField(auto_now_add=True, null=True)),
                ('datemodification', models.DateField(auto_now_add=True, null=True)),
                ('etat', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libellesite', models.CharField(max_length=255, null=True)),
                ('adressesite', models.CharField(max_length=255, null=True)),
                ('datecreationsite', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationsite', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatsite', models.BooleanField(default=False, null=True)),
                ('gerantsite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='TotalEmballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitedepotstockemballage', models.IntegerField(blank=True, null=True)),
                ('montantdepotstockemballage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantiterestantdepotstockemballage', models.IntegerField(blank=True, null=True)),
                ('montantrestantdepotstockemballage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('bb_12', models.IntegerField(default=0, null=True)),
                ('bb_24', models.IntegerField(default=0, null=True)),
                ('snb_12', models.IntegerField(default=0, null=True)),
                ('snb_24', models.IntegerField(default=0, null=True)),
                ('datecreationdepotstockemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationdepotstockemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatdepotstockemballage', models.BooleanField(default=False, null=True)),
                ('fournisseur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.fournisseur')),
                ('parametreprixemballage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.parametreprixemballage', verbose_name="Prix d'Emballage")),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.site')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='VenteProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitevendu', models.IntegerField(null=True, verbose_name='Quantité vendu')),
                ('montantvendu', models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Montant vendu')),
                ('acheteur', models.CharField(blank=True, max_length=100, null=True, verbose_name='Client particulier')),
                ('bb_12', models.IntegerField(default=0, null=True, verbose_name='Caiser bb de 12 prêté au client')),
                ('bb_24', models.IntegerField(default=0, null=True, verbose_name='Caiser bb de 24 prêté au client')),
                ('snb_12', models.IntegerField(default=0, null=True, verbose_name='Caiser snb de 12 prêté au client')),
                ('snb_24', models.IntegerField(default=0, null=True, verbose_name='Caiser snb de 24 prêté au client')),
                ('datecreation', models.DateField(auto_now_add=True, null=True)),
                ('datemodification', models.DateField(auto_now_add=True, null=True)),
                ('etat', models.BooleanField(default=False, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.client', verbose_name='Client régulier')),
                ('emballage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.totalemballage')),
                ('paramprixproduitvente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.paramprixproduitvente')),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.depotstockproduit')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.site')),
            ],
        ),
        migrations.CreateModel(
            name='RetournerEmballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bb_12', models.IntegerField(default=0, null=True, verbose_name='Caiser bb de 12 prêté au client')),
                ('bb_24', models.IntegerField(default=0, null=True, verbose_name='Caiser bb de 24 prêté au client')),
                ('snb_12', models.IntegerField(default=0, null=True, verbose_name='Caiser snb de 12 prêté au client')),
                ('snb_24', models.IntegerField(default=0, null=True, verbose_name='Caiser snb de 24 prêté au client')),
                ('datecreation', models.DateField(auto_now_add=True, null=True)),
                ('datemodification', models.DateField(auto_now_add=True, null=True)),
                ('etat', models.BooleanField(default=False, null=True)),
                ('venteproduit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.venteproduit')),
            ],
        ),
        migrations.CreateModel(
            name='RemboursementPoduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('totalpayer', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.depotstockproduit')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Profils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, null=True)),
                ('archive', models.BooleanField(default=False, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('droits', models.ManyToManyField(through='gestiondedepotapp.DroitsProfils', to='gestiondedepotapp.Droits')),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profil',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelleproduit', models.CharField(max_length=100, null=True)),
                ('formatproduit', models.CharField(choices=[('PM : Petit modèl', 'PM : Petit modèl'), ('GM : Grand modèl', 'GM : Grand modèl')], max_length=100, null=True)),
                ('contenanceproduit', models.IntegerField(null=True)),
                ('datecreationproduit', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationproduit', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatproduit', models.BooleanField(default=False, null=True)),
                ('categorieproduit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.categorieproduit')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='paramprixproduitvente',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.produit'),
        ),
        migrations.CreateModel(
            name='ParametrePrixAchatStockProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailprixproduit', models.CharField(choices=[('Casier entier', 'Casier entier'), ('Démi-casier', 'Démi-asier '), ('Quart de casier', 'Quart de casier')], max_length=20, null=True)),
                ('prixparametreprixachatstockproduit', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('datecreationparametreprixachatstockproduit', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationparametreprixachatstockproduit', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatparametreprixachatstockproduit', models.BooleanField(default=False, null=True)),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.produit')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='PanierStockProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_facture', models.CharField(blank=True, max_length=15, null=True, verbose_name='Numéro de facture')),
                ('quantitedepotstockproduit', models.IntegerField(null=True, verbose_name='Quantité dépot stock produit')),
                ('montantdepotstockproduit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nombrecasierequivalentdepotstockproduit', models.IntegerField(blank=True, help_text='24 bouteilles pour petit model et 12 bouteilles pour grand model', null=True)),
                ('quantiterestantdepotstockproduit', models.IntegerField(blank=True, null=True)),
                ('montantrestantdepotstockproduit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nombrecasierequivalentrestantdepotstockproduit', models.IntegerField(blank=True, help_text='24 bouteilles pour petit model et 12 bouteilles pour grand model', null=True)),
                ('casierperdu', models.IntegerField(default=0, null=True, verbose_name='Casier perdu')),
                ('produitperdu', models.IntegerField(default=0, null=True, verbose_name='Produit perdu')),
                ('casiercasse', models.IntegerField(default=0, null=True, verbose_name='Casier cassé')),
                ('produitcasse', models.IntegerField(default=0, null=True, verbose_name='Produit cassé')),
                ('panierdepot', models.BooleanField(default=True, null=True)),
                ('datecreationdepotstockproduit', models.DateField(auto_now_add=True, null=True)),
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
        migrations.CreateModel(
            name='PanierEmballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitedepotstockemballage', models.IntegerField(null=True)),
                ('montantdepotstockemballage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantiterestantdepotstockemballage', models.IntegerField(blank=True, null=True)),
                ('montantrestantdepotstockemballage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('panieremballage', models.BooleanField(default=True, null=True)),
                ('datecreationdepotstockemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationdepotstockemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatdepotstockemballage', models.BooleanField(default=False, null=True)),
                ('fournisseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.fournisseur')),
                ('parametreprixemballage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.parametreprixemballage', verbose_name="Prix d'Emballage")),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.site')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.site'),
        ),
        migrations.AddField(
            model_name='droitsprofils',
            name='profil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.profils'),
        ),
        migrations.AddField(
            model_name='depotstockproduit',
            name='fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.fournisseur'),
        ),
        migrations.AddField(
            model_name='depotstockproduit',
            name='parametreprixachatstockproduit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.parametreprixachatstockproduit', verbose_name='Produit prix'),
        ),
        migrations.AddField(
            model_name='depotstockproduit',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.site'),
        ),
        migrations.CreateModel(
            name='DepotStockEmballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitedepotstockemballage', models.IntegerField(null=True)),
                ('montantdepotstockemballage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantiterestantdepotstockemballage', models.IntegerField(blank=True, null=True)),
                ('montantrestantdepotstockemballage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('datecreationdepotstockemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('datemodificationdepotstockemballage', models.DateTimeField(auto_now_add=True, null=True)),
                ('etatdepotstockemballage', models.BooleanField(default=False, null=True)),
                ('fournisseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.fournisseur')),
                ('parametreprixemballage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.parametreprixemballage', verbose_name="Prix d'Emballage")),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.site')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Countwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_casier', models.IntegerField(blank=True, null=True, verbose_name='Total casier')),
                ('ancien', models.IntegerField(blank=True, null=True, verbose_name='Ancien total casier')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.site')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.site'),
        ),
        migrations.AddField(
            model_name='user',
            name='profil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestiondedepotapp.profils'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
