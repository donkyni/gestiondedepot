from django import forms
from django.utils.translation import ugettext_lazy as _

from gestiondedepotapp.models import CategorieProduit, Produit, Fournisseur, ParametrePrixAchatStockProduit, User, \
    Site, DepotStockProduit, Droits, Profils, DroitsProfils, Emballage, PanierEmballage, \
    ParametrePrixEmballage, PanierStockProduit, Count, RemboursementPoduit, ParamPrixProduitVente, Client, VenteProduit, \
    RetournerEmballage, PanierVente


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CategorieProduitForm(forms.ModelForm):
    class Meta:
        model = CategorieProduit
        fields = ('libellecategorieproduit',)

        widgets = {
            'libellecategorieproduit': forms.TextInput(attrs={'class': 'form-control'})
        }


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ('libelleproduit', 'formatproduit', 'contenanceproduit', 'categorieproduit', 'fournisseur')

        widgets = {
            'libelleproduit': forms.TextInput(attrs={'class': 'form-control'}),
            'formatproduit': forms.Select(attrs={'class': 'form-control'}),
            'categorieproduit': forms.Select(attrs={'class': 'form-control'})
        }


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields =('libellefournisseur', 'site', 'adressefournisseur', 'telephonefournisseur')

        widgets = {
            'libellefournisseur': forms.TextInput(attrs={'class': 'form-control'}),
            'site': forms.Select(attrs={'class': 'form-control'}),
            'adressefournisseur': forms.TextInput(attrs={'class': 'form-control'}),
            'telephonefournisseur': forms.TextInput(attrs={'class': 'form-control'})
        }


class ParametrePrixAchatStockProduitForm(forms.ModelForm):
    class Meta:
        model = ParametrePrixAchatStockProduit
        fields = ('produit', 'detailprixproduit', 'prixparametreprixachatstockproduit',)

        widgets = {
            'detailprixproduit': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
            'produit': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
        }


class DroitsForm(forms.ModelForm):
    class Meta:
        model = Droits
        fields = ('nom_du_droit',)


class ProfilsForm(forms.ModelForm):
    class Meta:
        model = Profils
        fields = ('nom',)
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'})
        }


class DroitsProfilsForm(forms.ModelForm):
    class Meta:
        model = DroitsProfils
        fields = ('profil', 'droit', 'ecriture', 'lecture', 'modification', 'suppression',)
        widgets = {
            'profil': forms.Select(attrs={'class': 'form-control'}),
            'droit': forms.Select(attrs={'class': 'form-control', 'selected': 'true'}),
            'ecriture': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'lecture': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'modification': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'suppression': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'pseudo', 'nom', 'prenom', 'adresse',
            'telephone', 'avatar', 'sexe',
        )
        widgets = {
            'pseudo': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    pseudo = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = (
            'pseudo', 'nom', 'prenom', 'adresse',
            'telephone', 'avatar', 'sexe',
        )
        widgets = {
            'pseudo': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'})
        }


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ('libellesite', 'adressesite', 'gerantsite',)

        widgets = {
            'libellesite': forms.TextInput(attrs={'class': 'form-control'}),
            'adressesite': forms.TextInput(attrs={'class': 'form-control'}),
            'gerantsite': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}),
        }


class CountForm(forms.ModelForm):
    class Meta:
        model = Count
        fields = ('bb_12', 'bb_24', 'snb_12', 'snb_24',)


class DepotStockProduitForm(forms.ModelForm):
    class Meta:
        model = DepotStockProduit
        fields = ('no_facture', 'fournisseur', 'parametreprixachatstockproduit', 'quantitedepotstockproduit', 'site',
                  'casierperdu', 'produitperdu', 'casiercasse', 'produitcasse')

        widgets = {
            'no_facture': forms.TextInput(attrs={'class': 'form-control'}),
            'fournisseur': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}),
            'parametreprixachatstockproduit': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}),
            'site': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}),
        }


class PanierStockProduitForm(forms.ModelForm):

    class Meta:
        model = PanierStockProduit
        fields = ('no_facture', 'fournisseur', 'parametreprixachatstockproduit', 'quantitedepotstockproduit', 'site',
                  'casierperdu', 'produitperdu', 'casiercasse', 'produitcasse')

        widgets = {
            'no_facture': forms.TextInput(attrs={'class': 'form-control'}),
            'fournisseur': forms.Select(attrs={'class': 'form-controls electpicker', 'data-live-search': 'true'}),
            'parametreprixachatstockproduit': forms.Select(attrs={'class': 'form-control selectpicker',
                                                                  'data-live-search': 'true'}),
            'site': forms.Select(attrs={'class': 'form-control'}),
        }


class EmballageForm(forms.ModelForm):
    class Meta:
        model = Emballage
        fields = ('libelleemballage', 'format', 'type')

        widgets = {
            'libelleemballage': forms.TextInput(attrs={'class': 'form-control'}),
            'format': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }


class ParametrePrixEmballageForm(forms.ModelForm):
    class Meta:
        model = ParametrePrixEmballage
        fields = ('emballage', 'prixparametreprixemballage',)

        widgets = {
            'emballage': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
        }


class PanierEmballageForm(forms.ModelForm):
    class Meta:
        model = PanierEmballage
        fields = ('fournisseur', 'parametreprixemballage', 'quantitedepotstockemballage', 'site')

        widgets = {
            'fournisseur': forms.Select(attrs={'class': 'form-control'}),
            'parametreprixemballage': forms.Select(attrs={'class': 'form-control'}),
            'site': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled'}),
        }


class HistoriquesAchatsForm(forms.ModelForm):
    requete_achat = forms.DateField(widget=DateInput, label="Sélectionner une date correspondant à l'achat :")

    class Meta:
        model = DepotStockProduit
        fields = ('no_facture', 'requete_achat',)
        widgets = {
            'no_facture': forms.TextInput(attrs={'class': 'form-control'})
        }


class RemboursementPoduitForm(forms.ModelForm):
    class Meta:
        model = RemboursementPoduit
        fields = ('produit', 'payer',)
        widgets = {
            'produit': forms.Select(attrs={'class': 'form-control'})
        }


"""
GESTION DES VENTES
"""


class ParamPrixProduitVenteForm(forms.ModelForm):
    class Meta:
        model = ParamPrixProduitVente
        fields = ('produit', 'detailprixvente', 'prixreelle', 'prixarrondi', 'remise',)
        widgets = {
            'produit': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
            'detailprixvente': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'})
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('libelleclient', 'adresse', 'contact', 'site',)
        widgets = {
            'site': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'})
        }


class VenteProduitForm(forms.ModelForm):
    class Meta:
        model = VenteProduit
        fields = ('no_facture', 'paramprixproduitvente', 'quantitevendu', 'client', 'acheteur', 'site',
                  'bb_12', 'bb_24', 'snb_12', 'snb_24')
        widgets = {
            'paramprixproduitvente': forms.Select(attrs={'class': 'form-control selectpicker',
                                                         'data-live-search': 'true'}),
            'client': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
            'site': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'})
        }


class PanierVenteForm(forms.ModelForm):
    class Meta:
        model = PanierVente
        fields = ('no_facture', 'paramprixproduitvente', 'quantitevendu', 'client', 'acheteur', 'site',
                  'bb_12', 'bb_24', 'snb_12', 'snb_24')
        labels = {
            'paramprixproduitvente': _('Produit'),
        }
        widgets = {
            'paramprixproduitvente': forms.Select(attrs={'class': 'form-control selectpicker',
                                                         'data-live-search': 'true'}),
            'client': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
            'site': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
            'acheteur': forms.TextInput(attrs={'placeholder': 'Laissez vide si vous avez sélectionner la case client'})
        }


class RetournerEmballageForm(forms.ModelForm):
    class Meta:
        model = RetournerEmballage
        fields = ('bb_12', 'bb_24', 'snb_12', 'snb_24', 'venteproduit',)
        widgets = {
            'venteproduit': forms.Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
        }
