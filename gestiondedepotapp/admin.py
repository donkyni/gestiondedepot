from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from gestiondedepotapp.models import CategorieProduit, Produit, Fournisseur, ParametrePrixAchatStockProduit, \
    DepotStockProduit, User, Site, Droits, Profils, DroitsProfils, Emballage, PanierEmballage, DepotStockEmballage, \
    ParametrePrixEmballage, PanierStockProduit, TotalEmballage, Count, Countwo, HistoriquesDesAchats, \
    RemboursementPoduit, ParamPrixProduitVente, Client, VenteProduit, RetournerEmballage, PanierVente, \
    TotalDepotStockProduit, RecupererFacture


class CategorieProduitAdmin(admin.ModelAdmin):
    list_display = ('libellecategorieproduit',
                    'datecreationcategorieproduit', 'datemodificationcategorieproduit', 'etatcategorieproduit')
    list_filter = ('libellecategorieproduit',)
    date_hierarchy = 'datecreationcategorieproduit'
    ordering = ('libellecategorieproduit',)
    search_fields = ('libellecategorieproduit',)


admin.site.register(CategorieProduit, CategorieProduitAdmin)


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('libelleproduit', 'formatproduit', 'contenanceproduit', 'categorieproduit',
                    'datecreationproduit', 'datemodificationproduit', 'etatproduit')
    list_filter = ('libelleproduit', 'formatproduit', 'contenanceproduit', 'categorieproduit',)
    date_hierarchy = 'datecreationproduit'
    ordering = ('libelleproduit',)
    search_fields = ('libelleproduit', 'formatproduit', 'contenanceproduit', 'categorieproduit',)


admin.site.register(Produit, ProduitAdmin)


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('libellefournisseur', 'site', 'adressefournisseur', 'telephonefournisseur',
                    'datecreationfournisseur', 'datemodificationfournisseur', 'etatfournisseur')
    list_filter = ('libellefournisseur', 'site',)
    date_hierarchy = 'datecreationfournisseur'
    ordering = ('libellefournisseur', 'site',)
    search_fields = ('libellefournisseur', 'site',)


admin.site.register(Fournisseur, FournisseurAdmin)


class ParametrePrixAchatStockProduitAdmin(admin.ModelAdmin):
    list_display = ('produit', 'prixparametreprixachatstockproduit',
                    'datecreationparametreprixachatstockproduit', 'datemodificationparametreprixachatstockproduit',
                    'etatparametreprixachatstockproduit')
    list_filter = ('produit', 'prixparametreprixachatstockproduit',)
    date_hierarchy = 'datecreationparametreprixachatstockproduit'
    ordering = ('produit',)
    search_fields = ('produit', 'prixparametreprixachatstockproduit',)


admin.site.register(ParametrePrixAchatStockProduit, ParametrePrixAchatStockProduitAdmin)


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'pseudo', 'nom', 'prenom', 'adresse',
            'telephone', 'avatar', 'sexe',
        )

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'pseudo', 'nom', 'prenom', 'adresse',
            'telephone', 'avatar', 'sexe', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class DroitsAdmin(admin.ModelAdmin):
    list_display = ('nom_du_droit', 'archive')
    list_filter = ('nom_du_droit',)
    ordering = ('nom_du_droit',)
    search_fields = ('nom_du_droit',)


admin.site.register(Droits, DroitsAdmin)


class ProfilsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'archive')
    list_filter = ('nom',)
    ordering = ('nom',)
    search_fields = ('nom',)


admin.site.register(Profils, ProfilsAdmin)


class DroitsProfilsAdmin(admin.ModelAdmin):
    list_display = ('profil', 'droit', 'ecriture', 'lecture', 'modification', 'suppression')
    list_filter = ('profil', 'droit')
    ordering = ('profil',)
    search_fields = ('profil',)


admin.site.register(DroitsProfils, DroitsProfilsAdmin)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        'pseudo', 'nom', 'prenom', 'adresse',
        'telephone', 'profil', 'avatar', 'sexe', 'is_admin', 'is_active')
    list_filter = ('is_admin', 'nom')
    fieldsets = (
        (None, {'fields': ('pseudo', 'password')}),
        ('Personal info', {'fields': (
            'nom', 'prenom', 'adresse',
            'telephone', 'avatar', 'sexe',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'pseudo', 'nom', 'prenom', 'adresse',
                'telephone', 'avatar', 'sexe', 'password'),
        }),
    )
    search_fields = ('pseudo', 'nom',)
    ordering = ('date_d_ajout',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)


class SiteAdmin(admin.ModelAdmin):
    list_display = ('libellesite', 'adressesite', 'gerantsite',
                    'datecreationsite', 'datemodificationsite', 'etatsite')
    list_filter = ('libellesite',)
    date_hierarchy = 'datecreationsite'
    ordering = ('libellesite', 'gerantsite',)
    search_fields = ('libellesite', 'gerantsite',)


admin.site.register(Site, SiteAdmin)


class DepotStockProduitAdmin(admin.ModelAdmin):
    list_display = ('no_facture', 'fournisseur', 'parametreprixachatstockproduit', 'quantitedepotstockproduit', 'site',
                    'casierperdu', 'produitperdu', 'casiercasse', 'produitcasse',
                    'montantdepotstockproduit', 'nombrecasierequivalentdepotstockproduit',
                    'quantiterestantdepotstockproduit', 'montantrestantdepotstockproduit',
                    'nombrecasierequivalentrestantdepotstockproduit',
                    'datecreationdepotstockproduit', 'datemodificationdepotstockproduit', 'etatdepotstockproduit')
    list_filter = ('fournisseur', 'parametreprixachatstockproduit', 'site',)
    date_hierarchy = 'datecreationdepotstockproduit'
    ordering = ('fournisseur', 'site',)
    search_fields = ('fournisseur', 'parametreprixachatstockproduit', 'site',)


admin.site.register(DepotStockProduit, DepotStockProduitAdmin)


class PanierStockProduitAdmin(admin.ModelAdmin):
    list_display = ('no_facture', 'fournisseur', 'parametreprixachatstockproduit', 'quantitedepotstockproduit', 'site',
                    'casierperdu', 'produitperdu', 'casiercasse', 'produitcasse',
                    'montantdepotstockproduit', 'nombrecasierequivalentdepotstockproduit',
                    'quantiterestantdepotstockproduit', 'montantrestantdepotstockproduit',
                    'nombrecasierequivalentrestantdepotstockproduit', 'panierdepot',
                    'datecreationdepotstockproduit', 'datemodificationdepotstockproduit', 'etatdepotstockproduit')
    list_filter = ('parametreprixachatstockproduit',)
    date_hierarchy = 'datecreationdepotstockproduit'
    ordering = ('parametreprixachatstockproduit',)
    search_fields = ('parametreprixachatstockproduit',)


class TotalDepotStockProduitAdmin(admin.ModelAdmin):
    list_display = ('fournisseur', 'parametreprixachatstockproduit', 'quantitedepotstockproduit', 'site',
                    'casierperdu', 'produitperdu', 'casiercasse', 'produitcasse',
                    'montantdepotstockproduit', 'nombrecasierequivalentdepotstockproduit',
                    'quantiterestantdepotstockproduit', 'montantrestantdepotstockproduit',
                    'nombrecasierequivalentrestantdepotstockproduit',
                    'datecreationdepotstockproduit', 'datemodificationdepotstockproduit', 'etatdepotstockproduit')
    list_filter = ('fournisseur', 'parametreprixachatstockproduit', 'site',)
    date_hierarchy = 'datecreationdepotstockproduit'
    ordering = ('fournisseur', 'site',)
    search_fields = ('fournisseur', 'parametreprixachatstockproduit', 'site',)


admin.site.register(TotalDepotStockProduit, TotalDepotStockProduitAdmin)


admin.site.register(PanierStockProduit, PanierStockProduitAdmin)


class EmballageAdmin(admin.ModelAdmin):
    list_display = ('libelleemballage', 'format', 'type',
                    'datecreationemballage', 'datemodificationemballage', 'etatemballage')
    list_filter = ('libelleemballage', 'format', 'type',)
    date_hierarchy = 'datecreationemballage'
    ordering = ('libelleemballage', 'format', 'type',)
    search_fields = ('libelleemballage', 'format', 'type',)


admin.site.register(Emballage, EmballageAdmin)


class ParametrePrixEmballageAdmin(admin.ModelAdmin):
    list_display = ('emballage', 'prixparametreprixemballage',
                    'datecreationparametreprixemballage', 'datemodificationparametreprixemballage',
                    'etatparametreprixemballage')
    list_filter = ('emballage', 'prixparametreprixemballage',)
    date_hierarchy = 'datecreationparametreprixemballage'
    ordering = ('emballage',)
    search_fields = ('emballage', 'prixparametreprixemballage',)


admin.site.register(ParametrePrixEmballage, ParametrePrixEmballageAdmin)


class DepotStockEmballageAdmin(admin.ModelAdmin):
    list_display = ('site', 'fournisseur', 'parametreprixemballage', 'quantitedepotstockemballage',
                    'montantdepotstockemballage', 'quantiterestantdepotstockemballage',
                    'montantrestantdepotstockemballage',
                    'datecreationdepotstockemballage', 'datemodificationdepotstockemballage', 'etatdepotstockemballage')
    list_filter = ('site', 'parametreprixemballage',)
    date_hierarchy = 'datecreationdepotstockemballage'
    ordering = ('site', 'parametreprixemballage',)
    search_fields = ('site', 'parametreprixemballage',)


class PanierEmballageAdmin(admin.ModelAdmin):
    list_display = ('site', 'fournisseur', 'parametreprixemballage', 'quantitedepotstockemballage',
                    'montantdepotstockemballage', 'quantiterestantdepotstockemballage',
                    'montantrestantdepotstockemballage', 'panieremballage',
                    'datecreationdepotstockemballage', 'datemodificationdepotstockemballage', 'etatdepotstockemballage')
    list_filter = ('site', 'parametreprixemballage',)
    date_hierarchy = 'datecreationdepotstockemballage'
    ordering = ('site', 'parametreprixemballage',)
    search_fields = ('site', 'parametreprixemballage',)


admin.site.register(PanierEmballage, PanierEmballageAdmin)


class TotalEmballageAdmin(admin.ModelAdmin):
    list_display = ('site', 'fournisseur', 'parametreprixemballage', 'quantitedepotstockemballage',
                    'montantdepotstockemballage', 'quantiterestantdepotstockemballage',
                    'montantrestantdepotstockemballage',
                    'datecreationdepotstockemballage', 'datemodificationdepotstockemballage', 'etatdepotstockemballage')
    list_filter = ('site', 'parametreprixemballage',)
    date_hierarchy = 'datecreationdepotstockemballage'
    ordering = ('site', 'parametreprixemballage',)
    search_fields = ('site', 'parametreprixemballage',)


admin.site.register(TotalEmballage, TotalEmballageAdmin)


class RecupererFactureAdmin(admin.ModelAdmin):
    list_display = ('recup_facture_bb', 'recup_facture_bb')
    list_filter = ('date',)
    ordering = ('date',)
    search_fields = ('date',)


admin.site.register(RecupererFacture, RecupererFactureAdmin)


class CountAdmin(admin.ModelAdmin):
    list_display = ('bb_12', 'bb_24', 'snb_12', 'snb_24', 'etat')
    list_filter = ('etat',)
    ordering = ('etat',)
    search_fields = ('etat',)


admin.site.register(Count, CountAdmin)


class CountwoAdmin(admin.ModelAdmin):
    list_display = ('site', 'total_casier', 'ancien')
    list_filter = ('site', 'total_casier',)
    ordering = ('site', 'total_casier',)
    search_fields = ('site', 'total_casier',)


admin.site.register(Countwo, CountwoAdmin)


class HistoriquesDesAchatsAdmin(admin.ModelAdmin):
    list_display = ('no_facture', 'date_achat')
    list_filter = ('no_facture', 'date_achat')
    ordering = ('no_facture', 'date_achat')
    search_fields = ('no_facture' 'date_achat',)


admin.site.register(HistoriquesDesAchats, HistoriquesDesAchatsAdmin)


class RemboursementPoduitAdmin(admin.ModelAdmin):
    list_display = ('produit', 'payer', 'totalpayer')
    list_filter = ('payer',)
    date_hierarchy = 'date'
    ordering = ('produit',)
    search_fields = ('produit',)


admin.site.register(RemboursementPoduit, RemboursementPoduitAdmin)


class ParamPrixProduitVenteAdmin(admin.ModelAdmin):
    list_display = ('produit', 'detailprixvente', 'prixreelle', 'prixarrondi', 'remise', 'datecreation',
                    'datemodification', 'etat')
    list_filter = ('produit', 'detailprixvente', 'prixreelle', 'remise')
    date_hierarchy = 'datecreation'
    ordering = ('produit', 'prixreelle', 'remise')
    search_fields = ('produit', 'prixreelle', 'remise')


admin.site.register(ParamPrixProduitVente, ParamPrixProduitVenteAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('libelleclient', 'adresse', 'contact', 'site',
                    'datecreation', 'datemodification', 'etat')
    list_filter = ('libelleclient', 'adresse', 'site')
    date_hierarchy = 'datecreation'
    ordering = ('libelleclient', 'adresse', 'site')
    search_fields = ('libelleclient', 'adresse', 'site')


admin.site.register(Client, ClientAdmin)


class VenteProduitAdmin(admin.ModelAdmin):
    list_display = ('paramprixproduitvente', 'quantitevendu', 'montantvendu', 'client', 'acheteur', 'site', 'bb_12',
                    'bb_24', 'snb_12', 'snb_24',
                    'datecreation', 'datemodification', 'etat')
    list_filter = ('paramprixproduitvente', 'client', 'acheteur', 'site')
    date_hierarchy = 'datecreation'
    ordering = ('paramprixproduitvente', 'client', 'acheteur', 'site')
    search_fields = ('paramprixproduitvente', 'client', 'acheteur', 'site')


admin.site.register(VenteProduit, VenteProduitAdmin)


class PanierVenteAdmin(admin.ModelAdmin):
    list_display = ('paramprixproduitvente', 'quantitevendu', 'montantvendu', 'client', 'acheteur', 'site', 'bb_12',
                    'bb_24', 'snb_12', 'snb_24', 'paniervente',
                    'datecreation', 'datemodification', 'etat')
    list_filter = ('paramprixproduitvente', 'client', 'acheteur', 'site')
    date_hierarchy = 'datecreation'
    ordering = ('paramprixproduitvente', 'client', 'acheteur', 'site')
    search_fields = ('paramprixproduitvente', 'client', 'acheteur', 'site')


admin.site.register(PanierVente, PanierVenteAdmin)


class RetournerEmballageAdmin(admin.ModelAdmin):
    list_display = ('bb_12', 'bb_24', 'snb_12', 'snb_24', 'venteproduit',
                    'datecreation', 'datemodification', 'etat')
    list_filter = ('bb_12', 'bb_24', 'snb_12', 'snb_24', 'venteproduit',)
    date_hierarchy = 'datecreation'
    ordering = ('bb_12', 'bb_24', 'snb_12', 'snb_24', 'venteproduit',)
    search_fields = ('bb_12', 'bb_24', 'snb_12', 'snb_24', 'venteproduit',)


admin.site.register(RetournerEmballage, RetournerEmballageAdmin)
