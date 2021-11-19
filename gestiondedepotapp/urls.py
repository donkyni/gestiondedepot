from django.conf.urls import url

from gestiondedepotapp import views

urlpatterns = [
    url(r'^tableaudebord$', views.tableaudebord, name="tableaudebord"),
    url(r'^details-concernant-le-site-1', views.site1, name="site1"),
    url(r'^details-concernant-le-site-2', views.site2, name="site2"),
    url(r'^details-concernant-le-site-3', views.site3, name="site3"),
    url(r'^categorie$', views.categorie, name="categorie"),
    url(r'^ajoutercategorie$', views.ajoutercategorie, name="ajoutercategorie"),
    url(r'^(?P<id>\d+)/modifiercategorie$', views.modifiercategorie, name="modifiercategorie"),
    url(r'^(?P<id>\d+)/supprimercategorie', views.supprimercategorie, name="supprimercategorie"),
    url(r'^site$', views.site, name="site"),
    url(r'^ajoutersite$', views.ajoutersite, name="ajoutersite"),
    url(r'^(?P<id>\d+)/modifiersite$', views.modifiersite, name="modifiersite"),
    url(r'^(?P<id>\d+)/supprimersite$', views.supprimersite, name="supprimersite"),
    url(r'^produit$', views.produit, name="produit"),
    url(r'^ajouterproduit$', views.ajouterproduit, name="ajouterproduit"),
    url(r'^(?P<id>\d+)/modifierproduit$', views.modifierproduit, name="modifierproduit"),
    url(r'^(?P<id>\d+)/suprimerproduit$', views.supprimerproduit, name="supprimerproduit"),

    # Param prix produit
    url(r'^parametre-prix-produit', views.paramprixproduit, name="paramprixproduit"),
    url(r'^ajouter-param-prix-produit$', views.ajouterparamprixproduit, name="ajouterparamprixproduit"),
    url(r'^(?P<id>\d+)/modifier-param-prix-produit$', views.modifierparamprixproduit, name="modifierparamprixproduit"),
    url(r'^(?P<id>\d+)/supprimer-param-prix-produit$', views.supprimerparamprixproduit,
        name="supprimerparamprixproduit"),

    url(r'^fournisseur', views.fournisseur, name="fournisseur"),
    url(r'^ajouter-un-fournisseur$', views.ajouterfournisseur, name="ajouterfournisseur"),
    url(r'^(?P<id>\d+)/modifier-un-fournisseur$', views.modifierfournisseur, name="modifierfournisseur"),
    url(r'^(?P<id>\d+)/supprimer-un-fournisseur$', views.supprimerfournisseur, name="supprimerfournisseur"),
    # utilisateurs route
    url(r'^compte', views.compte, name="compte"),
    url(r'^utilisateur', views.utilisateur, name="utilisateur"),
    url(r'^ajouter-un-utilisateur', views.ajouterutilisateur, name="ajouterutilisateur"),
    url(r'^(?P<id>\d+)/modifier-un-utilisateur', views.modifierutilisateur, name="modifierutilisateur"),
    url(r'^(?P<id>\d+)/supprimer-un-utilisateur', views.supprimerutilisateur, name="supprimerutilisateur"),
    url(r'^(?P<id>\d+)/activez-un-utilisateur', views.activezutilisateur, name="activezutilisateur"),
    # droits route
    url(r'^droit', views.droit, name="droit"),
    url(r'^ajouter-un-droit', views.ajouterdroit, name="ajouterdroit"),
    url(r'^(?P<id>\d+)/modifier-un-droit', views.modifierdroit, name="modifierdroit"),
    url(r'^(?P<id>\d+)/supprimer-un-droit', views.supprimerdroit, name="supprimerdroit"),
    # profils route
    url(r'^profil', views.profil, name="profil"),
    url(r'^ajouter-un-profil', views.ajouterprofil, name="ajouterprofil"),
    url(r'^(?P<id>\d+)/modifier-un-profil', views.modifierprofil, name="modifierprofil"),
    url(r'^(?P<id>\d+)/supprimer-un-profil', views.supprimerprofil, name="supprimerprofil"),

    # routes concernant le stock
    url(r'^panier-des-depots-de-produit', views.panierdepot, name="panierdepot"),
    url(r'^depot-de-stock', views.depotstock, name="depotstock"),
    url(r'^historique-des-achats', views.historique_des_achats, name="historique_des_achats"),
    url(r'^achats-de-requete', views.achats_de_requete, name="achats_de_requete"),
    url(r'^gestion-des-pertes', views.pertes, name="pertes"),
    url(r'^(?P<id>\d+)/rembourser-une-perte', views.pertesrembourser, name="pertesrembourser"),
    url(r'^table-depot-de-stock', views.tabledepotstock, name="tabledepotstock"),
    url(r'^ajout-depot-de-stock', views.ajoutdepot, name="ajoutdepot"),
    url(r'^(?P<id>\d+)/modifier-un-stock$', views.modifiertabledepotstock, name="modifiertabledepotstock"),
    url(r'^(?P<id>\d+)/supprimer-un-stock$', views.supprimertabledepotstock, name="supprimertabledepotstock"),
    url(r'^petit-model-dans-la-table-des-stocks', views.petitmodel, name="petitmodel"),
    url(r'^grand-model-dans-la-table-des-stocks', views.grandmodel, name="grandmodel"),

    # emballage
    url(r'^panier-des-emballages', views.panieremaballage, name='panieremballage'),
    url(r'^gestion-des-emballages', views.emballage, name='emballage'),
    url(r'^insertion-des-emballages-dans-le-panier', views.tableemballagestock, name='tableemballagestock'),

    # emballages
    url(r'^emballages', views.embal, name="embal"),
    url(r'^ajouter-un-emballage$', views.ajouterembal, name="ajouterembal"),
    url(r'^(?P<id>\d+)/modifier-un-emballage$', views.modifierembal, name="modifierembal"),
    url(r'^(?P<id>\d+)/supprimer-un-emballage$', views.supprimerembal, name="supprimerembal"),

    # param prix emballages
    url(r'^parametres-prix-emballages', views.paramembal, name="paramembal"),
    url(r'^ajouter-param-prix-emballages$', views.ajouterparamembal, name="ajouterparamembal"),
    url(r'^(?P<id>\d+)/modifier-param-prix-emballage$', views.modifierparamembal, name="modifierparamembal"),
    url(r'^(?P<id>\d+)/supprimer-param-prix-emballage$', views.supprimerparamprixproduit, name="supprimerparamembal"),

    # ####################################### VENTE ##########################################

    url(r'^vente', views.vente, name="vente"),
    # CLIENTS
    url(r'^client', views.client, name="client"),
    url(r'^ajouter-un-client$', views.ajouterclient, name="ajouterclient"),
    url(r'^(?P<id>\d+)/modifier-un-client$', views.modifierclient, name="modifierclient"),
    url(r'^(?P<id>\d+)/supprimer-un-client$', views.supprimerclient, name="supprimerclient"),
    # PARAMETRE DE PRIX DE VENTE
    url(r'^paramprixvente', views.paramprixvente, name="paramprixvente"),
    url(r'^ajouter-un-paramètre-de-prix-de-vente$', views.ajouterparamprixvente, name="ajouterparamprixvente"),
    url(r'^(?P<id>\d+)/modifier-un-paramètre-de-prix-de-vente$',
        views.modifierparamprixvente, name="modifierparamprixvente"),
    url(r'^(?P<id>\d+)/supprimer-un-paramètre-de-prix-de-vente$',
        views.supprimerparamprixvente, name="supprimerparamprixvente"),
    # VENTE DE PRODUIT
    url(r'^panier-des-ventes', views.paniervente, name="paniervente"),
    # EMBALLAGE CONSIGNE
    url(r'^embalconsigne', views.embalconsigne, name="embalconsigne"),
    url(r'^depot', views.depot, name="depot"),

]
