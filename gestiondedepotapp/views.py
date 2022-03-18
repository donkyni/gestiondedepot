from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect

from gestiondedepotapp.forms import CategorieProduitForm, SiteForm, ProduitForm, ParametrePrixAchatStockProduitForm, \
    FournisseurForm, DepotStockProduitForm, UserCreationForm, UserUpdateForm, DroitsForm, ProfilsForm, \
    PanierEmballageForm, ParametrePrixEmballageForm, EmballageForm, PanierStockProduitForm, \
    CountForm, HistoriquesAchatsForm, RemboursementPoduitForm, ClientForm, ParamPrixProduitVenteForm, PanierVenteForm
from gestiondedepotapp.models import CategorieProduit, Site, Produit, ParametrePrixAchatStockProduit, Fournisseur, \
    DepotStockProduit, User, Droits, Profils, PanierEmballage, DepotStockEmballage, ParametrePrixEmballage, Emballage, \
    PanierStockProduit, TotalEmballage, Count, Countwo, HistoriquesDesAchats, RemboursementPoduit, Client, \
    ParamPrixProduitVente, PanierVente


@login_required
def save_all(request, form, template_name, model, template_name2, mycontext):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            if model == "categorie":
                systeme = form.save(commit=False)
                systeme.datemodificationcategorieproduit = datetime.now()
                systeme.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "site":
                systeme = form.save(commit=False)
                systeme.datemodificationsite = datetime.now()
                systeme.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "produit":
                systeme = form.save(commit=False)
                systeme.datemodificationproduit = datetime.now()
                systeme.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "paramprixproduit":
                systeme = form.save(commit=False)
                systeme.datemodificationparametreprixachatstockproduit = datetime.now()
                systeme.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "fournisseur":
                systeme = form.save(commit=False)
                systeme.datemodificationfournisseur = datetime.now()
                systeme.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "utilisateur":
                form.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "droit":
                form.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "profil":
                form.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "paramembal":
                systeme = form.save(commit=False)
                systeme.datemodificationparametreprixemballage = datetime.now()
                systeme.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "embal":
                systeme = form.save(commit=False)
                systeme.datemodificationemballage = datetime.now()
                systeme.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "client":
                systeme = form.save(commit=False)
                systeme.datemodification = datetime.now()
                systeme.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
            if model == "paramprixvente":
                systeme = form.save(commit=False)
                systeme.datemodification = datetime.now()
                systeme.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
        else:
            data['form_is_valid'] = False

    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def tableaudebord(request):
    site1 = get_object_or_404(Site, libellesite="SITE 1")
    site2 = get_object_or_404(Site, libellesite="SITE 2")
    site3 = get_object_or_404(Site, libellesite="SITE 3")
    totalproduitsite1 = DepotStockProduit.objects.filter(site=site1).count()
    totalproduitsite2 = DepotStockProduit.objects.filter(site=site2).count()
    totalproduitsite3 = DepotStockProduit.objects.filter(site=site3).count()
    totalemballagesite1 = TotalEmballage.objects.filter(site=site1).count()
    totalemballagesite2 = TotalEmballage.objects.filter(site=site2).count()
    totalemballagesite3 = TotalEmballage.objects.filter(site=site3).count()
    context = {
        'site1': site1,
        'site2': site2,
        'site3': site3,
        'totalproduitsite1': totalproduitsite1,
        'totalproduitsite2': totalproduitsite2,
        'totalproduitsite3': totalproduitsite3,
        'totalemballagesite1': totalemballagesite1,
        'totalemballagesite2': totalemballagesite2,
        'totalemballagesite3': totalemballagesite3,
    }
    return render(request, 'gestiondedepotapp/templates/tableaudebord.html', context)


@login_required
def site1(request):
    gerant = "SITE 1"
    gerant_site = get_object_or_404(Site, libellesite=gerant)

    """ Petit model total """
    quantitestockpm = 0
    quantitestockpmrestant = 0
    casierstockpm = 0
    casierstockpmrestant = 0
    montantstockpm = 0
    montantstockpmrestant = 0
    stocks_pm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "PM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)
    for depotpm in stocks_pm:
        quantitestockpm += depotpm.quantitedepotstockproduit
        quantitestockpmrestant += depotpm.quantiterestantdepotstockproduit
        montantstockpm += depotpm.montantdepotstockproduit
        montantstockpmrestant += depotpm.montantrestantdepotstockproduit
        casierstockpm += depotpm.nombrecasierequivalentdepotstockproduit
        casierstockpmrestant += depotpm.nombrecasierequivalentrestantdepotstockproduit

    """ Grand model total """
    quantitestockgm = 0
    quantitestockgmrestant = 0
    casierstockgm = 0
    casierstockgmrestant = 0
    montantstockgm = 0
    montantstockgmrestant = 0
    montantstockrestant = 0

    stocks_gm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "GM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)

    for depotgm in stocks_gm:
        quantitestockgm += depotgm.quantitedepotstockproduit
        quantitestockgmrestant += depotgm.quantiterestantdepotstockproduit
        montantstockgm += depotgm.montantdepotstockproduit
        montantstockgmrestant += depotgm.montantrestantdepotstockproduit
        casierstockgm += depotgm.nombrecasierequivalentdepotstockproduit
        casierstockgmrestant += depotgm.nombrecasierequivalentrestantdepotstockproduit
    ############################################################################################

    """ GRAND MODEL """

    quantitestockbeaufort = 0
    quantitestockrestantbeaufort = 0
    casierstockbeaufort = 0
    casierstockrestantbeaufort = 0
    montantstockbeaufort = 0
    montantstockrestantbeaufort = 0

    quantitestockawouyo = 0
    quantitestockrestantawouyo = 0
    casierstockawouyo = 0
    casierstockrestantawouyo = 0
    montantstockawouyo = 0
    montantstockrestantawouyo = 0

    quantitestockcoca = 0
    quantitestockrestantcoca = 0
    casierstockcoca = 0
    casierstockrestantcoca = 0
    montantstockcoca = 0
    montantstockrestantcoca = 0

    quantitestockfanta = 0
    quantitestockrestantfanta = 0
    casierstockfanta = 0
    casierstockrestantfanta = 0
    montantstockfanta = 0
    montantstockrestantfanta = 0

    quantitestocklager = 0
    quantitestockrestantlager = 0
    casierstocklager = 0
    casierstockrestantlager = 0
    montantstocklager = 0
    montantstockrestantlager = 0

    """ PETIT MODEL """

    quantitestockbeaufortpm = 0
    quantitestockrestantbeaufortpm = 0
    casierstockbeaufortpm = 0
    casierstockrestantbeaufortpm = 0
    montantstockbeaufortpm = 0
    montantstockrestantbeaufortpm = 0

    quantitestockawouyopm = 0
    quantitestockrestantawouyopm = 0
    casierstockawouyopm = 0
    casierstockrestantawouyopm = 0
    montantstockawouyopm = 0
    montantstockrestantawouyopm = 0

    quantitestockcocapm = 0
    quantitestockrestantcocapm = 0
    casierstockcocapm = 0
    casierstockrestantcocapm = 0
    montantstockcocapm = 0
    montantstockrestantcocapm = 0

    quantitestockfantapm = 0
    quantitestockrestantfantapm = 0
    casierstockfantapm = 0
    casierstockrestantfantapm = 0
    montantstockfantapm = 0
    montantstockrestantfantapm = 0

    quantitestocklagerpm = 0
    quantitestockrestantlagerpm = 0
    casierstocklagerpm = 0
    casierstockrestantlagerpm = 0
    montantstocklagerpm = 0
    montantstockrestantlagerpm = 0

    ####################################################################################################
    """ LES PRODUITS GRANDS MODEL """

    # GRAND MODEL : BEAUFORT
    beaufort = get_object_or_404(Produit, formatproduit="GM", libelleproduit="BEAUFORT")
    beaufort_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufort,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_beaufort in beaufort_stock:
        quantitestockbeaufort += depot_beaufort.quantitedepotstockproduit
        quantitestockrestantbeaufort += depot_beaufort.quantiterestantdepotstockproduit
        montantstockbeaufort += depot_beaufort.montantdepotstockproduit
        montantstockrestantbeaufort += depot_beaufort.montantrestantdepotstockproduit
        casierstockbeaufort += depot_beaufort.nombrecasierequivalentdepotstockproduit
        casierstockrestantbeaufort += depot_beaufort.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # GRAND MODEL : AWOUYO
    awouyo = get_object_or_404(Produit, formatproduit="GM", libelleproduit="AWOUYO")
    awouyo_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyo,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_awouyo in awouyo_stock:
        quantitestockawouyo += depot_awouyo.quantitedepotstockproduit
        quantitestockrestantawouyo += depot_awouyo.quantiterestantdepotstockproduit
        montantstockawouyo += depot_awouyo.montantdepotstockproduit
        montantstockrestantawouyo += depot_awouyo.montantrestantdepotstockproduit
        casierstockawouyo += depot_awouyo.nombrecasierequivalentdepotstockproduit
        casierstockrestantawouyo += depot_awouyo.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # GRAND MODEL : COCA
    coca = get_object_or_404(Produit, formatproduit="GM", libelleproduit="COCA")
    coca_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=coca,
                                                  site=gerant_site,
                                                  etatdepotstockproduit=False)

    for depot_coca in coca_stock:
        quantitestockcoca += depot_coca.quantitedepotstockproduit
        quantitestockrestantcoca += depot_coca.quantiterestantdepotstockproduit
        montantstockcoca += depot_coca.montantdepotstockproduit
        montantstockrestantcoca += depot_coca.montantrestantdepotstockproduit
        casierstockcoca += depot_coca.nombrecasierequivalentdepotstockproduit
        casierstockrestantcoca += depot_coca.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # GRAND MODEL : FANTA
    fanta = get_object_or_404(Produit, formatproduit="GM", libelleproduit="FANTA")
    fanta_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fanta,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_fanta in fanta_stock:
        quantitestockfanta += depot_fanta.quantitedepotstockproduit
        montantstockfanta += depot_fanta.montantdepotstockproduit
        casierstockfanta += depot_fanta.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfanta += depot_fanta.quantiterestantdepotstockproduit
        montantstockrestantfanta += depot_fanta.montantrestantdepotstockproduit
        casierstockrestantfanta += depot_fanta.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # GRAND MODEL : LAGER
    lager = get_object_or_404(Produit, formatproduit="GM", libelleproduit="LAGER")
    lager_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lager,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_lager in lager_stock:
        quantitestocklager += depot_lager.quantitedepotstockproduit
        montantstocklager += depot_lager.montantdepotstockproduit
        casierstocklager += depot_lager.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlager += depot_lager.quantiterestantdepotstockproduit
        montantstockrestantlager += depot_lager.montantrestantdepotstockproduit
        casierstockrestantlager += depot_lager.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    #####################################################################################################
    """ LES PRODUITS PETITS MODEL """

    # PETIT MODEL : BEAUFORT
    beaufortpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="BEAUFORT")
    beaufort_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufortpm,
                                                        site=gerant_site,
                                                        etatdepotstockproduit=False)

    for depot_beaufort_pm in beaufort_stockpm:
        quantitestockbeaufortpm += depot_beaufort_pm.quantitedepotstockproduit
        quantitestockrestantbeaufortpm += depot_beaufort_pm.quantiterestantdepotstockproduit
        montantstockbeaufortpm += depot_beaufort_pm.montantdepotstockproduit
        montantstockrestantbeaufortpm += depot_beaufort_pm.montantrestantdepotstockproduit
        casierstockbeaufortpm += depot_beaufort_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantbeaufortpm += depot_beaufort_pm.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # PETIT MODEL : AWOUYO
    awouyopm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="AWOUYO")
    awouyo_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyopm,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_awouyo_pm in awouyo_stockpm:
        quantitestockawouyopm += depot_awouyo_pm.quantitedepotstockproduit
        quantitestockrestantawouyopm += depot_awouyo_pm.quantiterestantdepotstockproduit
        montantstockawouyopm += depot_awouyo_pm.montantdepotstockproduit
        montantstockrestantawouyopm += depot_awouyo_pm.montantrestantdepotstockproduit
        casierstockawouyopm += depot_awouyo_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantawouyopm += depot_awouyo_pm.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # PETIT MODEL : COCA
    cocapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="COCA")
    coca_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=cocapm,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_coca_pm in coca_stockpm:
        quantitestockcocapm += depot_coca_pm.quantitedepotstockproduit
        quantitestockrestantcocapm += depot_coca_pm.quantiterestantdepotstockproduit
        montantstockcocapm += depot_coca_pm.montantdepotstockproduit
        montantstockrestantcocapm += depot_coca_pm.montantrestantdepotstockproduit
        casierstockcocapm += depot_coca_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantcocapm += depot_coca_pm.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # PETIT MODEL : FANTA
    fantapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="FANTA")
    fanta_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fantapm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_fanta_pm in fanta_stockpm:
        quantitestockfantapm += depot_fanta_pm.quantitedepotstockproduit
        montantstockfantapm += depot_fanta_pm.montantdepotstockproduit
        casierstockfantapm += depot_fanta_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfantapm += depot_fanta_pm.quantiterestantdepotstockproduit
        montantstockrestantfantapm += depot_fanta_pm.montantrestantdepotstockproduit
        casierstockrestantfantapm += depot_fanta_pm.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # PETIT MODEL : LAGER
    lagerpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="LAGER")
    lager_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lagerpm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_lager_pm in lager_stockpm:
        quantitestocklagerpm += depot_lager_pm.quantitedepotstockproduit
        montantstocklagerpm += depot_lager_pm.montantdepotstockproduit
        casierstocklagerpm += depot_lager_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlagerpm += depot_lager_pm.quantiterestantdepotstockproduit
        montantstockrestantlagerpm += depot_lager_pm.montantrestantdepotstockproduit
        casierstockrestantlagerpm += depot_lager_pm.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    """ Total Emballages """
    casier12bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="12",
                                   parametreprixemballage__emballage__type="BB")
    if casier12bb is not None:
        restant12bb = casier12bb.quantitedepotstockemballage - casier12bb.quantiterestantdepotstockemballage

    casier24bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="24",
                                   parametreprixemballage__emballage__type="BB")
    if casier24bb is not None:
        restant24bb = casier24bb.quantitedepotstockemballage - casier24bb.quantiterestantdepotstockemballage

    casier12snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="12",
                                    parametreprixemballage__emballage__type="SNB")
    if casier12snb is not None:
        restant12snb = casier12snb.quantitedepotstockemballage - casier12snb.quantiterestantdepotstockemballage

    casier24snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="24",
                                    parametreprixemballage__emballage__type="SNB")
    if casier24snb is not None:
        restant24snb = casier24snb.quantitedepotstockemballage - casier24snb.quantiterestantdepotstockemballage

    return render(request, 'gestiondedepotapp/templates/site1.html', locals())


@login_required
def site2(request):
    gerant = "SITE 2"
    gerant_site = get_object_or_404(Site, libellesite=gerant)
    print(gerant_site)

    """ Petit model total """
    quantitestockpm = 0
    quantitestockpmrestant = 0
    casierstockpm = 0
    casierstockpmrestant = 0
    montantstockpm = 0
    montantstockpmrestant = 0
    stocks_pm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "PM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)
    for depotpm in stocks_pm:
        quantitestockpm += depotpm.quantitedepotstockproduit
        quantitestockpmrestant += depotpm.quantiterestantdepotstockproduit
        montantstockpm += depotpm.montantdepotstockproduit
        montantstockpmrestant += depotpm.montantrestantdepotstockproduit
        casierstockpm += depotpm.nombrecasierequivalentdepotstockproduit
        casierstockpmrestant += depotpm.nombrecasierequivalentrestantdepotstockproduit

    """ Grand model total """
    quantitestockgm = 0
    quantitestockgmrestant = 0
    casierstockgm = 0
    casierstockgmrestant = 0
    montantstockgm = 0
    montantstockgmrestant = 0
    montantstockrestant = 0

    stocks_gm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "GM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)

    for depotgm in stocks_gm:
        quantitestockgm += depotgm.quantitedepotstockproduit
        quantitestockgmrestant += depotgm.quantiterestantdepotstockproduit
        montantstockgm += depotgm.montantdepotstockproduit
        montantstockgmrestant += depotgm.montantrestantdepotstockproduit
        casierstockgm += depotgm.nombrecasierequivalentdepotstockproduit
        casierstockgmrestant += depotgm.nombrecasierequivalentrestantdepotstockproduit
    ############################################################################################

    """ GRAND MODEL """

    quantitestockbeaufort = 0
    quantitestockrestantbeaufort = 0
    casierstockbeaufort = 0
    casierstockrestantbeaufort = 0
    montantstockbeaufort = 0
    montantstockrestantbeaufort = 0

    quantitestockawouyo = 0
    quantitestockrestantawouyo = 0
    casierstockawouyo = 0
    casierstockrestantawouyo = 0
    montantstockawouyo = 0
    montantstockrestantawouyo = 0

    quantitestockcoca = 0
    quantitestockrestantcoca = 0
    casierstockcoca = 0
    casierstockrestantcoca = 0
    montantstockcoca = 0
    montantstockrestantcoca = 0

    quantitestockfanta = 0
    quantitestockrestantfanta = 0
    casierstockfanta = 0
    casierstockrestantfanta = 0
    montantstockfanta = 0
    montantstockrestantfanta = 0

    quantitestocklager = 0
    quantitestockrestantlager = 0
    casierstocklager = 0
    casierstockrestantlager = 0
    montantstocklager = 0
    montantstockrestantlager = 0

    """ PETIT MODEL """

    quantitestockbeaufortpm = 0
    quantitestockrestantbeaufortpm = 0
    casierstockbeaufortpm = 0
    casierstockrestantbeaufortpm = 0
    montantstockbeaufortpm = 0
    montantstockrestantbeaufortpm = 0

    quantitestockawouyopm = 0
    quantitestockrestantawouyopm = 0
    casierstockawouyopm = 0
    casierstockrestantawouyopm = 0
    montantstockawouyopm = 0
    montantstockrestantawouyopm = 0

    quantitestockcocapm = 0
    quantitestockrestantcocapm = 0
    casierstockcocapm = 0
    casierstockrestantcocapm = 0
    montantstockcocapm = 0
    montantstockrestantcocapm = 0

    quantitestockfantapm = 0
    quantitestockrestantfantapm = 0
    casierstockfantapm = 0
    casierstockrestantfantapm = 0
    montantstockfantapm = 0
    montantstockrestantfantapm = 0

    quantitestocklagerpm = 0
    quantitestockrestantlagerpm = 0
    casierstocklagerpm = 0
    casierstockrestantlagerpm = 0
    montantstocklagerpm = 0
    montantstockrestantlagerpm = 0

    ####################################################################################################
    """ LES PRODUITS GRANDS MODEL """

    # GRAND MODEL : BEAUFORT
    beaufort = get_object_or_404(Produit, formatproduit="GM", libelleproduit="BEAUFORT")
    beaufort_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufort,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_beaufort in beaufort_stock:
        quantitestockbeaufort += depot_beaufort.quantitedepotstockproduit
        quantitestockrestantbeaufort += depot_beaufort.quantiterestantdepotstockproduit
        montantstockbeaufort += depot_beaufort.montantdepotstockproduit
        montantstockrestantbeaufort += depot_beaufort.montantrestantdepotstockproduit
        casierstockbeaufort += depot_beaufort.nombrecasierequivalentdepotstockproduit
        casierstockrestantbeaufort += depot_beaufort.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # GRAND MODEL : AWOUYO
    awouyo = get_object_or_404(Produit, formatproduit="GM", libelleproduit="AWOUYO")
    awouyo_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyo,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_awouyo in awouyo_stock:
        quantitestockawouyo += depot_awouyo.quantitedepotstockproduit
        quantitestockrestantawouyo += depot_awouyo.quantiterestantdepotstockproduit
        montantstockawouyo += depot_awouyo.montantdepotstockproduit
        montantstockrestantawouyo += depot_awouyo.montantrestantdepotstockproduit
        casierstockawouyo += depot_awouyo.nombrecasierequivalentdepotstockproduit
        casierstockrestantawouyo += depot_awouyo.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # GRAND MODEL : COCA
    coca = get_object_or_404(Produit, formatproduit="GM", libelleproduit="COCA")
    coca_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=coca,
                                                  site=gerant_site,
                                                  etatdepotstockproduit=False)

    for depot_coca in coca_stock:
        quantitestockcoca += depot_coca.quantitedepotstockproduit
        quantitestockrestantcoca += depot_coca.quantiterestantdepotstockproduit
        montantstockcoca += depot_coca.montantdepotstockproduit
        montantstockrestantcoca += depot_coca.montantrestantdepotstockproduit
        casierstockcoca += depot_coca.nombrecasierequivalentdepotstockproduit
        casierstockrestantcoca += depot_coca.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # GRAND MODEL : FANTA
    fanta = get_object_or_404(Produit, formatproduit="GM", libelleproduit="FANTA")
    fanta_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fanta,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_fanta in fanta_stock:
        quantitestockfanta += depot_fanta.quantitedepotstockproduit
        montantstockfanta += depot_fanta.montantdepotstockproduit
        casierstockfanta += depot_fanta.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfanta += depot_fanta.quantiterestantdepotstockproduit
        montantstockrestantfanta += depot_fanta.montantrestantdepotstockproduit
        casierstockrestantfanta += depot_fanta.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # GRAND MODEL : LAGER
    lager = get_object_or_404(Produit, formatproduit="GM", libelleproduit="LAGER")
    lager_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lager,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_lager in lager_stock:
        quantitestocklager += depot_lager.quantitedepotstockproduit
        montantstocklager += depot_lager.montantdepotstockproduit
        casierstocklager += depot_lager.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlager += depot_lager.quantiterestantdepotstockproduit
        montantstockrestantlager += depot_lager.montantrestantdepotstockproduit
        casierstockrestantlager += depot_lager.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    #####################################################################################################
    """ LES PRODUITS PETITS MODEL """

    # PETIT MODEL : BEAUFORT
    beaufortpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="BEAUFORT")
    beaufort_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufortpm,
                                                        site=gerant_site,
                                                        etatdepotstockproduit=False)

    for depot_beaufort_pm in beaufort_stockpm:
        quantitestockbeaufortpm += depot_beaufort_pm.quantitedepotstockproduit
        quantitestockrestantbeaufortpm += depot_beaufort_pm.quantiterestantdepotstockproduit
        montantstockbeaufortpm += depot_beaufort_pm.montantdepotstockproduit
        montantstockrestantbeaufortpm += depot_beaufort_pm.montantrestantdepotstockproduit
        casierstockbeaufortpm += depot_beaufort_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantbeaufortpm += depot_beaufort_pm.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # PETIT MODEL : AWOUYO
    awouyopm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="AWOUYO")
    awouyo_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyopm,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_awouyo_pm in awouyo_stockpm:
        quantitestockawouyopm += depot_awouyo_pm.quantitedepotstockproduit
        quantitestockrestantawouyopm += depot_awouyo_pm.quantiterestantdepotstockproduit
        montantstockawouyopm += depot_awouyo_pm.montantdepotstockproduit
        montantstockrestantawouyopm += depot_awouyo_pm.montantrestantdepotstockproduit
        casierstockawouyopm += depot_awouyo_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantawouyopm += depot_awouyo_pm.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # PETIT MODEL : COCA
    cocapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="COCA")
    coca_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=cocapm,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_coca_pm in coca_stockpm:
        quantitestockcocapm += depot_coca_pm.quantitedepotstockproduit
        quantitestockrestantcocapm += depot_coca_pm.quantiterestantdepotstockproduit
        montantstockcocapm += depot_coca_pm.montantdepotstockproduit
        montantstockrestantcocapm += depot_coca_pm.montantrestantdepotstockproduit
        casierstockcocapm += depot_coca_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantcocapm += depot_coca_pm.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # PETIT MODEL : FANTA
    fantapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="FANTA")
    fanta_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fantapm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_fanta_pm in fanta_stockpm:
        quantitestockfantapm += depot_fanta_pm.quantitedepotstockproduit
        montantstockfantapm += depot_fanta_pm.montantdepotstockproduit
        casierstockfantapm += depot_fanta_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfantapm += depot_fanta_pm.quantiterestantdepotstockproduit
        montantstockrestantfantapm += depot_fanta_pm.montantrestantdepotstockproduit
        casierstockrestantfantapm += depot_fanta_pm.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # PETIT MODEL : LAGER
    lagerpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="LAGER")
    lager_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lagerpm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_lager_pm in lager_stockpm:
        quantitestocklagerpm += depot_lager_pm.quantitedepotstockproduit
        montantstocklagerpm += depot_lager_pm.montantdepotstockproduit
        casierstocklagerpm += depot_lager_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlagerpm += depot_lager_pm.quantiterestantdepotstockproduit
        montantstockrestantlagerpm += depot_lager_pm.montantrestantdepotstockproduit
        casierstockrestantlagerpm += depot_lager_pm.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    """ Total Emballages """
    casier12bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="12",
                                   parametreprixemballage__emballage__type="BB")
    if casier12bb is not None:
        restant12bb = casier12bb.quantitedepotstockemballage - casier12bb.quantiterestantdepotstockemballage

    casier24bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="24",
                                   parametreprixemballage__emballage__type="BB")
    if casier24bb is not None:
        restant24bb = casier24bb.quantitedepotstockemballage - casier24bb.quantiterestantdepotstockemballage

    casier12snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="12",
                                    parametreprixemballage__emballage__type="SNB")
    if casier12snb is not None:
        restant12snb = casier12snb.quantitedepotstockemballage - casier12snb.quantiterestantdepotstockemballage

    casier24snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="24",
                                    parametreprixemballage__emballage__type="SNB")
    if casier24snb is not None:
        restant24snb = casier24snb.quantitedepotstockemballage - casier24snb.quantiterestantdepotstockemballage

    return render(request, 'gestiondedepotapp/templates/site2.html', locals())


@login_required
def site3(request):
    gerant = "SITE 3"
    gerant_site = get_object_or_404(Site, libellesite=gerant)

    """ Petit model total """
    quantitestockpm = 0
    quantitestockpmrestant = 0
    casierstockpm = 0
    casierstockpmrestant = 0
    montantstockpm = 0
    montantstockpmrestant = 0
    stocks_pm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "PM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)
    for depotpm in stocks_pm:
        quantitestockpm += depotpm.quantitedepotstockproduit
        quantitestockpmrestant += depotpm.quantiterestantdepotstockproduit
        montantstockpm += depotpm.montantdepotstockproduit
        montantstockpmrestant += depotpm.montantrestantdepotstockproduit
        casierstockpm += depotpm.nombrecasierequivalentdepotstockproduit
        casierstockpmrestant += depotpm.nombrecasierequivalentrestantdepotstockproduit

    """ Grand model total """
    quantitestockgm = 0
    quantitestockgmrestant = 0
    casierstockgm = 0
    casierstockgmrestant = 0
    montantstockgm = 0
    montantstockgmrestant = 0
    montantstockrestant = 0

    stocks_gm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "GM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)

    for depotgm in stocks_gm:
        quantitestockgm += depotgm.quantitedepotstockproduit
        quantitestockgmrestant += depotgm.quantiterestantdepotstockproduit
        montantstockgm += depotgm.montantdepotstockproduit
        montantstockgmrestant += depotgm.montantrestantdepotstockproduit
        casierstockgm += depotgm.nombrecasierequivalentdepotstockproduit
        casierstockgmrestant += depotgm.nombrecasierequivalentrestantdepotstockproduit
    ############################################################################################

    """ GRAND MODEL """

    quantitestockbeaufort = 0
    quantitestockrestantbeaufort = 0
    casierstockbeaufort = 0
    casierstockrestantbeaufort = 0
    montantstockbeaufort = 0
    montantstockrestantbeaufort = 0

    quantitestockawouyo = 0
    quantitestockrestantawouyo = 0
    casierstockawouyo = 0
    casierstockrestantawouyo = 0
    montantstockawouyo = 0
    montantstockrestantawouyo = 0

    quantitestockcoca = 0
    quantitestockrestantcoca = 0
    casierstockcoca = 0
    casierstockrestantcoca = 0
    montantstockcoca = 0
    montantstockrestantcoca = 0

    quantitestockfanta = 0
    quantitestockrestantfanta = 0
    casierstockfanta = 0
    casierstockrestantfanta = 0
    montantstockfanta = 0
    montantstockrestantfanta = 0

    quantitestocklager = 0
    quantitestockrestantlager = 0
    casierstocklager = 0
    casierstockrestantlager = 0
    montantstocklager = 0
    montantstockrestantlager = 0

    """ PETIT MODEL """

    quantitestockbeaufortpm = 0
    quantitestockrestantbeaufortpm = 0
    casierstockbeaufortpm = 0
    casierstockrestantbeaufortpm = 0
    montantstockbeaufortpm = 0
    montantstockrestantbeaufortpm = 0

    quantitestockawouyopm = 0
    quantitestockrestantawouyopm = 0
    casierstockawouyopm = 0
    casierstockrestantawouyopm = 0
    montantstockawouyopm = 0
    montantstockrestantawouyopm = 0

    quantitestockcocapm = 0
    quantitestockrestantcocapm = 0
    casierstockcocapm = 0
    casierstockrestantcocapm = 0
    montantstockcocapm = 0
    montantstockrestantcocapm = 0

    quantitestockfantapm = 0
    quantitestockrestantfantapm = 0
    casierstockfantapm = 0
    casierstockrestantfantapm = 0
    montantstockfantapm = 0
    montantstockrestantfantapm = 0

    quantitestocklagerpm = 0
    quantitestockrestantlagerpm = 0
    casierstocklagerpm = 0
    casierstockrestantlagerpm = 0
    montantstocklagerpm = 0
    montantstockrestantlagerpm = 0

    ####################################################################################################
    """ LES PRODUITS GRANDS MODEL """

    # GRAND MODEL : BEAUFORT
    beaufort = get_object_or_404(Produit, formatproduit="GM", libelleproduit="BEAUFORT")
    beaufort_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufort,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_beaufort in beaufort_stock:
        quantitestockbeaufort += depot_beaufort.quantitedepotstockproduit
        quantitestockrestantbeaufort += depot_beaufort.quantiterestantdepotstockproduit
        montantstockbeaufort += depot_beaufort.montantdepotstockproduit
        montantstockrestantbeaufort += depot_beaufort.montantrestantdepotstockproduit
        casierstockbeaufort += depot_beaufort.nombrecasierequivalentdepotstockproduit
        casierstockrestantbeaufort += depot_beaufort.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # GRAND MODEL : AWOUYO
    awouyo = get_object_or_404(Produit, formatproduit="GM", libelleproduit="AWOUYO")
    awouyo_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyo,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_awouyo in awouyo_stock:
        quantitestockawouyo += depot_awouyo.quantitedepotstockproduit
        quantitestockrestantawouyo += depot_awouyo.quantiterestantdepotstockproduit
        montantstockawouyo += depot_awouyo.montantdepotstockproduit
        montantstockrestantawouyo += depot_awouyo.montantrestantdepotstockproduit
        casierstockawouyo += depot_awouyo.nombrecasierequivalentdepotstockproduit
        casierstockrestantawouyo += depot_awouyo.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # GRAND MODEL : COCA
    coca = get_object_or_404(Produit, formatproduit="GM", libelleproduit="COCA")
    coca_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=coca,
                                                  site=gerant_site,
                                                  etatdepotstockproduit=False)

    for depot_coca in coca_stock:
        quantitestockcoca += depot_coca.quantitedepotstockproduit
        quantitestockrestantcoca += depot_coca.quantiterestantdepotstockproduit
        montantstockcoca += depot_coca.montantdepotstockproduit
        montantstockrestantcoca += depot_coca.montantrestantdepotstockproduit
        casierstockcoca += depot_coca.nombrecasierequivalentdepotstockproduit
        casierstockrestantcoca += depot_coca.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # GRAND MODEL : FANTA
    fanta = get_object_or_404(Produit, formatproduit="GM", libelleproduit="FANTA")
    fanta_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fanta,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_fanta in fanta_stock:
        quantitestockfanta += depot_fanta.quantitedepotstockproduit
        montantstockfanta += depot_fanta.montantdepotstockproduit
        casierstockfanta += depot_fanta.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfanta += depot_fanta.quantiterestantdepotstockproduit
        montantstockrestantfanta += depot_fanta.montantrestantdepotstockproduit
        casierstockrestantfanta += depot_fanta.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # GRAND MODEL : LAGER
    lager = get_object_or_404(Produit, formatproduit="GM", libelleproduit="LAGER")
    lager_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lager,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_lager in lager_stock:
        quantitestocklager += depot_lager.quantitedepotstockproduit
        montantstocklager += depot_lager.montantdepotstockproduit
        casierstocklager += depot_lager.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlager += depot_lager.quantiterestantdepotstockproduit
        montantstockrestantlager += depot_lager.montantrestantdepotstockproduit
        casierstockrestantlager += depot_lager.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    #####################################################################################################
    """ LES PRODUITS PETITS MODEL """

    # PETIT MODEL : BEAUFORT
    beaufortpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="BEAUFORT")
    beaufort_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufortpm,
                                                        site=gerant_site,
                                                        etatdepotstockproduit=False)

    for depot_beaufort_pm in beaufort_stockpm:
        quantitestockbeaufortpm += depot_beaufort_pm.quantitedepotstockproduit
        quantitestockrestantbeaufortpm += depot_beaufort_pm.quantiterestantdepotstockproduit
        montantstockbeaufortpm += depot_beaufort_pm.montantdepotstockproduit
        montantstockrestantbeaufortpm += depot_beaufort_pm.montantrestantdepotstockproduit
        casierstockbeaufortpm += depot_beaufort_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantbeaufortpm += depot_beaufort_pm.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # PETIT MODEL : AWOUYO
    awouyopm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="AWOUYO")
    awouyo_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyopm,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_awouyo_pm in awouyo_stockpm:
        quantitestockawouyopm += depot_awouyo_pm.quantitedepotstockproduit
        quantitestockrestantawouyopm += depot_awouyo_pm.quantiterestantdepotstockproduit
        montantstockawouyopm += depot_awouyo_pm.montantdepotstockproduit
        montantstockrestantawouyopm += depot_awouyo_pm.montantrestantdepotstockproduit
        casierstockawouyopm += depot_awouyo_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantawouyopm += depot_awouyo_pm.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # PETIT MODEL : COCA
    cocapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="COCA")
    coca_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=cocapm,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_coca_pm in coca_stockpm:
        quantitestockcocapm += depot_coca_pm.quantitedepotstockproduit
        quantitestockrestantcocapm += depot_coca_pm.quantiterestantdepotstockproduit
        montantstockcocapm += depot_coca_pm.montantdepotstockproduit
        montantstockrestantcocapm += depot_coca_pm.montantrestantdepotstockproduit
        casierstockcocapm += depot_coca_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantcocapm += depot_coca_pm.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # PETIT MODEL : FANTA
    fantapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="FANTA")
    fanta_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fantapm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_fanta_pm in fanta_stockpm:
        quantitestockfantapm += depot_fanta_pm.quantitedepotstockproduit
        montantstockfantapm += depot_fanta_pm.montantdepotstockproduit
        casierstockfantapm += depot_fanta_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfantapm += depot_fanta_pm.quantiterestantdepotstockproduit
        montantstockrestantfantapm += depot_fanta_pm.montantrestantdepotstockproduit
        casierstockrestantfantapm += depot_fanta_pm.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # PETIT MODEL : LAGER
    lagerpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="LAGER")
    lager_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lagerpm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_lager_pm in lager_stockpm:
        quantitestocklagerpm += depot_lager_pm.quantitedepotstockproduit
        montantstocklagerpm += depot_lager_pm.montantdepotstockproduit
        casierstocklagerpm += depot_lager_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlagerpm += depot_lager_pm.quantiterestantdepotstockproduit
        montantstockrestantlagerpm += depot_lager_pm.montantrestantdepotstockproduit
        casierstockrestantlagerpm += depot_lager_pm.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    """ Total Emballages """
    casier12bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="12",
                                   parametreprixemballage__emballage__type="BB")
    if casier12bb is not None:
        restant12bb = casier12bb.quantitedepotstockemballage - casier12bb.quantiterestantdepotstockemballage

    casier24bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="24",
                                   parametreprixemballage__emballage__type="BB")
    if casier24bb is not None:
        restant24bb = casier24bb.quantitedepotstockemballage - casier24bb.quantiterestantdepotstockemballage

    casier12snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="12",
                                    parametreprixemballage__emballage__type="SNB")
    if casier12snb is not None:
        restant12snb = casier12snb.quantitedepotstockemballage - casier12snb.quantiterestantdepotstockemballage

    casier24snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="24",
                                    parametreprixemballage__emballage__type="SNB")
    if casier24snb is not None:
        restant24snb = casier24snb.quantitedepotstockemballage - casier24snb.quantiterestantdepotstockemballage

    return render(request, 'gestiondedepotapp/templates/site3.html', locals())


@login_required
def categorie(request):
    categories = CategorieProduit.objects.filter(etatcategorieproduit=False)
    context = {
        'categories': categories,
    }
    return render(request, 'gestiondedepotapp/templates/categorie/categorie.html', context)


@login_required
def ajoutercategorie(request):
    categories = CategorieProduit.objects.filter(etatcategorieproduit=False)

    context = {'categories': categories}

    if request.method == 'POST':
        form = CategorieProduitForm(request.POST)
    else:
        form = CategorieProduitForm()

    return save_all(request, form, 'gestiondedepotapp/templates/categorie/ajoutercategorie.html',
                    'categorie', 'gestiondedepotapp/templates/categorie/listecategorie.html', context)


@login_required
def modifiercategorie(request, id):
    categories = CategorieProduit.objects.filter(etatcategorieproduit=False)
    mycontext = {
        'categories': categories
    }
    categorie = get_object_or_404(CategorieProduit, id=id)
    if request.method == 'POST':
        form = CategorieProduitForm(request.POST, instance=categorie)
    else:
        form = CategorieProduitForm(instance=categorie)
    return save_all(request, form, 'gestiondedepotapp/templates/categorie/modifiercategorie.html', 'categorie',
                    'gestiondedepotapp/templates/categorie/listecategorie.html', mycontext)


@login_required
def supprimercategorie(request, id):
    data = dict()
    categorie = get_object_or_404(CategorieProduit, id=id)
    if request.method == "POST":
        categorie.archive = True
        categorie.save()
        data['form_is_valid'] = True
        categories = CategorieProduit.objects.filter(etatcategorieproduit=False)
        data['categorie'] = render_to_string('gestiondedepotapp/templates/categorie/listecategorie.html',
                                             {'categories': categories})
    else:
        context = {
            'categorie': categorie,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/categorie/supprimercategorie.html', context,
                                             request=request)

    return JsonResponse(data)


@login_required
def site(request):
    sites = Site.objects.filter(etatsite=False)
    context = {
        'sites': sites,
    }
    return render(request, 'gestiondedepotapp/templates/site/site.html', context)


@login_required
def ajoutersite(request):
    sites = Site.objects.filter(etatsite=False)

    context = {'sites': sites}

    form = SiteForm(request.POST) if request.method == 'POST' else SiteForm()
    return save_all(request, form, 'gestiondedepotapp/templates/site/ajoutersite.html',
                    'site', 'gestiondedepotapp/templates/site/listesite.html', context)


@login_required
def modifiersite(request, id):
    sites = Site.objects.filter(etatsite=False)
    mycontext = {
        'sites': sites
    }
    site = get_object_or_404(Site, id=id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
    else:
        form = SiteForm(instance=site)
    return save_all(request, form, 'gestiondedepotapp/templates/site/modifiersite.html', 'site',
                    'gestiondedepotapp/templates/site/listesite.html', mycontext)


@login_required
def supprimersite(request, id):
    data = dict()
    site = get_object_or_404(Site, id=id)
    if request.method == "POST":
        site.etatsite = True
        site.save()
        data['form_is_valid'] = True
        sites = Site.objects.filter(etatsite=False)
        data['site'] = render_to_string('gestiondedepotapp/templates/site/listesite.html',
                                        {'sites': sites})
    else:
        context = {
            'site': site,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/site/supprimersite.html', context,
                                             request=request)

    return JsonResponse(data)


@login_required
def produit(request):
    produits = Produit.objects.filter(etatproduit=False)
    context = {
        'produits': produits,
    }
    return render(request, 'gestiondedepotapp/templates/produit/produit.html', context)


@login_required
def ajouterproduit(request):
    produits = Produit.objects.filter(etatproduit=False)

    context = {'produits': produits}

    form = ProduitForm(request.POST) if request.method == 'POST' else ProduitForm()
    return save_all(request, form, 'gestiondedepotapp/templates/produit/ajouterproduit.html',
                    'produit', 'gestiondedepotapp/templates/produit/listeproduit.html', context)


@login_required
def modifierproduit(request, id):
    produits = Produit.objects.filter(etatproduit=False)
    mycontext = {
        'produits': produits
    }
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
    else:
        form = ProduitForm(instance=produit)
    return save_all(request, form, 'gestiondedepotapp/templates/produit/modifierproduit.html', 'produit',
                    'gestiondedepotapp/templates/produit/listeproduit.html', mycontext)


@login_required
def supprimerproduit(request, id):
    data = dict()
    produit = get_object_or_404(Produit, id=id)
    if request.method == "POST":
        produit.etatproduit = True
        produit.save()
        data['form_is_valid'] = True
        produits = Produit.objects.filter(etatproduit=False)
        data['produit'] = render_to_string('gestiondedepotapp/templates/produit/listeproduit.html',
                                           {'produits': produits})
    else:
        context = {
            'produit': produit,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/produit/supprimerproduit.html', context,
                                             request=request)

    return JsonResponse(data)


@login_required
def paramprixproduit(request):
    paramprixproduits = ParametrePrixAchatStockProduit.objects.filter(etatparametreprixachatstockproduit=False)
    context = {
        'paramprixproduits': paramprixproduits,
    }
    return render(request, 'gestiondedepotapp/templates/paramprixproduit/paramprixproduit.html', context)


@login_required
def ajouterparamprixproduit(request):
    paramprixproduits = ParametrePrixAchatStockProduit.objects.filter(etatparametreprixachatstockproduit=False)

    context = {'paramprixproduits': paramprixproduits}

    if request.method == 'POST':
        form = ParametrePrixAchatStockProduitForm(request.POST)
    else:
        form = ParametrePrixAchatStockProduitForm()

    return save_all(request, form, 'gestiondedepotapp/templates/paramprixproduit/ajouterparamprixproduit.html',
                    'paramprixproduit', 'gestiondedepotapp/templates/paramprixproduit/listeparamprixproduit.html',
                    context)


@login_required
def modifierparamprixproduit(request, id):
    paramprixproduits = ParametrePrixAchatStockProduit.objects.filter(etatparametreprixachatstockproduit=False)
    mycontext = {
        'paramprixproduits': paramprixproduits
    }
    paramprixproduit = get_object_or_404(ParametrePrixAchatStockProduit, id=id)
    if request.method == 'POST':
        form = ParametrePrixAchatStockProduitForm(request.POST, instance=paramprixproduit)
    else:
        form = ParametrePrixAchatStockProduitForm(instance=paramprixproduit)
    return save_all(request, form, 'gestiondedepotapp/templates/paramprixproduit/modifierparamprixproduit.html',
                    'paramprixproduit',
                    'gestiondedepotapp/templates/paramprixproduit/listeparamprixproduit.html', mycontext)


@login_required
def supprimerparamprixproduit(request, id):
    data = dict()
    paramprixproduit = get_object_or_404(ParametrePrixAchatStockProduit, id=id)
    if request.method == "POST":
        paramprixproduit.etatparametreprixachatstockproduit = True
        paramprixproduit.save()
        data['form_is_valid'] = True
        paramprixproduits = ParametrePrixAchatStockProduit.objects.filter(etatparametreprixachatstockproduit=False)
        data['paramprixproduit'] = render_to_string('gestiondedepotapp/templates/paramprixproduit'
                                                    '/listeparamprixproduit.html',
                                                    {'paramprixproduits': paramprixproduits})
    else:
        context = {
            'paramprixproduit': paramprixproduit,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/paramprixproduit/supprimerparamprixproduit.html',
                                             context,
                                             request=request)

    return JsonResponse(data)


@login_required
def fournisseur(request):
    fournisseurs = Fournisseur.objects.filter(etatfournisseur=False)
    context = {
        'fournisseurs': fournisseurs,
    }
    return render(request, 'gestiondedepotapp/templates/fournisseur/fournisseur.html', context)


@login_required
def ajouterfournisseur(request):
    fournisseurs = Fournisseur.objects.filter(etatfournisseur=False)

    context = {'fournisseurs': fournisseurs}

    if request.method == 'POST':
        form = FournisseurForm(request.POST)
    else:
        form = FournisseurForm()

    return save_all(request, form, 'gestiondedepotapp/templates/fournisseur/ajouterfournisseur.html',
                    'fournisseur', 'gestiondedepotapp/templates/fournisseur/listefournisseur.html',
                    context)


@login_required
def modifierfournisseur(request, id):
    fournisseurs = Fournisseur.objects.filter(etatfournisseur=False)
    mycontext = {
        'fournisseurs': fournisseurs
    }
    fournisseur = get_object_or_404(Fournisseur, id=id)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
    else:
        form = FournisseurForm(instance=fournisseur)
    return save_all(request, form, 'gestiondedepotapp/templates/fournisseur/modifierfournisseur.html',
                    'fournisseur',
                    'gestiondedepotapp/templates/fournisseur/listefournisseur.html', mycontext)


@login_required
def supprimerfournisseur(request, id):
    data = dict()
    fournisseur = get_object_or_404(Fournisseur, id=id)
    if request.method == "POST":
        fournisseur.etatfournisseur = True
        fournisseur.save()
        data['form_is_valid'] = True
        fournisseurs = Fournisseur.objects.filter(etatfournisseur=False)
        data['fournisseur'] = render_to_string('gestiondedepotapp/templates/fournisseur'
                                               '/listefournisseur.html',
                                               {'fournisseurs': fournisseurs})
    else:
        context = {
            'fournisseur': fournisseur,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/fournisseur/supprimerfournisseur'
                                             '.html', context,
                                             request=request)

    return JsonResponse(data)


@login_required
def compte(request):
    user = request.user
    site = get_object_or_404(Site, gerantsite=user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user)
        if u_form.is_valid():
            u_form.save()
            redirect('compte')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
        'site': site,
    }
    return render(request, 'gestiondedepotapp/templates/utilisateur/compte.html', context)


@login_required
def utilisateur(request):
    utilisateurs = User.objects.all()
    context = {
        'utilisateurs': utilisateurs
    }
    return render(request, 'gestiondedepotapp/templates/utilisateur/utilisateur.html', context)


@login_required
def ajouterutilisateur(request):
    utilisateurs = User.objects.all()

    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
    else:
        form = UserCreationForm()
    context = {
        'utilisateurs': utilisateurs
    }
    return save_all(request, form, 'gestiondedepotapp/templates/utilisateur/ajouterutilisateur.html',
                    'utilisateur', 'gestiondedepotapp/templates/utilisateur/listeutilisateur.html', context)


@login_required
def modifierutilisateur(request, id):
    utilisateurs = User.objects.all()

    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
    else:
        form = UserUpdateForm(instance=user)

    context = {
        'utilisateurs': utilisateurs
    }
    return save_all(request, form, 'gestiondedepotapp/templates/utilisateur/modifierutilisateur.html',
                    'utilisateur', 'gestiondedepotapp/templates/utilisateur/listeutilisateur.html', context)


@login_required
def supprimerutilisateur(request, id):
    utilisateur = get_object_or_404(User, id=id)
    data = {}

    if request.method == 'POST':
        utilisateur.is_active = False
        utilisateur.save()
        data['form_is_valid'] = True
        utilisateurs = User.objects.all()
        data['utilisateur'] = render_to_string('gestiondedepotapp/templates/utilisateur/listeutilisateur.html',
                                               {'utilisateurs': utilisateurs})
    else:
        context = {
            'utilisateur': utilisateur,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/utilisateur/supprimerutilisateur.html',
                                             context,
                                             request=request)

    return JsonResponse(data)


@login_required
def activezutilisateur(request, id):
    utilisateur = get_object_or_404(User, id=id)
    data = {}

    if request.method == 'POST':
        utilisateur.is_active = True
        utilisateur.save()
        data['form_is_valid'] = True
        utilisateurs = User.objects.all()
        data['utilisateur'] = render_to_string('gestiondedepotapp/templates/utilisateur/listeutilisateur.html',
                                               {'utilisateurs': utilisateurs})
    else:
        context = {
            'utilisateur': utilisateur,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/utilisateur/activezutilisateur.html',
                                             context,
                                             request=request)

    return JsonResponse(data)


@login_required
def droit(request):
    droits = Droits.objects.filter(archive=False)
    context = {
        'droits': droits,
    }
    return render(request, 'gestiondedepotapp/templates/droit/droit.html', context)


@login_required
def ajouterdroit(request):
    droits = Droits.objects.filter(archive=False)

    context = {'droits': droits}

    form = DroitsForm(request.POST) if request.method == 'POST' else DroitsForm()
    return save_all(request, form, 'gestiondedepotapp/templates/droit/ajouterdroit.html',
                    'droit', 'gestiondedepotapp/templates/droit/listedroit.html', context)


@login_required
def modifierdroit(request, id):
    droits = Droits.objects.filter(archive=False)
    mycontext = {
        'droits': droits
    }
    droit = get_object_or_404(Droits, id=id)
    if request.method == 'POST':
        form = DroitsForm(request.POST, instance=droit)
    else:
        form = DroitsForm(instance=droit)
    return save_all(request, form, 'gestiondedepotapp/templates/droit/modifierdroit.html', 'droit',
                    'gestiondedepotapp/templates/droit/listedroit.html', mycontext)


@login_required
def supprimerdroit(request, id):
    data = dict()
    droit = get_object_or_404(Droits, id=id)
    if request.method == "POST":
        droit.archive = True
        droit.save()
        data['form_is_valid'] = True
        droits = Droits.objects.filter(archive=False)
        data['droit'] = render_to_string('gestiondedepotapp/templates/droit/listedroit.html',
                                         {'droits': droits})
    else:
        context = {
            'droit': droit,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/droit/supprimerdroit.html', context,
                                             request=request)

    return JsonResponse(data)


@login_required
def profil(request):
    profils = Profils.objects.filter(archive=False)
    context = {
        'profils': profils,
    }
    return render(request, 'gestiondedepotapp/templates/profil/profil.html', context)


@login_required
def ajouterprofil(request):
    profils = Profils.objects.filter(archive=False)

    context = {'profils': profils}

    form = ProfilsForm(request.POST) if request.method == 'POST' else ProfilsForm()
    return save_all(request, form, 'gestiondedepotapp/templates/profil/ajouterprofil.html',
                    'profil', 'gestiondedepotapp/templates/profil/listeprofil.html', context)


@login_required
def modifierprofil(request, id):
    profils = Profils.objects.filter(archive=False)
    mycontext = {
        'profils': profils
    }
    profil = get_object_or_404(Profils, id=id)
    if request.method == 'POST':
        form = ProfilsForm(request.POST, instance=profil)
    else:
        form = ProfilsForm(instance=profil)
    return save_all(request, form, 'gestiondedepotapp/templates/profil/modifierprofil.html', 'profil',
                    'gestiondedepotapp/templates/profil/listeprofil.html', mycontext)


@login_required
def supprimerprofil(request, id):
    data = dict()
    profil = get_object_or_404(Droits, id=id)
    if request.method == "POST":
        profil.archive = True
        profil.save()
        data['form_is_valid'] = True
        profils = Droits.objects.filter(archive=False)
        data['profil'] = render_to_string('gestiondedepotapp/templates/profil/listeprofil.html',
                                          {'profils': profils})
    else:
        context = {
            'profil': profil,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/profil/supprimerprofil.html', context,
                                             request=request)

    return JsonResponse(data)


@login_required
def depotstock(request):
    gerant = request.user
    gerant_site = get_object_or_404(Site, gerantsite=gerant)

    """casier12bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="12",
                                   parametreprixemballage__emballage__type="BB")

    casier24bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="24",
                                   parametreprixemballage__emballage__type="BB")

    casier12snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="12",
                                    parametreprixemballage__emballage__type="SNB")

    casier24snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="24",
                                    parametreprixemballage__emballage__type="SNB")

    casier_total_emporter = casier12bb.bb_12 + casier24bb.bb_24 + casier12snb.snb_12 + casier24snb.snb_24

    casier_equivalent = get_object_or_404(Countwo, site=gerant_site)"""

    quantitestock = 0
    quantitestockrestant = 0
    casierstock = 0
    casierstockrestant = 0
    montantstock = 0
    montantstockrestant = 0

    quantitestockgm = 0
    quantitestockgmrestant = 0
    casierstockgm = 0
    casierstockgmrestant = 0
    montantstockgm = 0
    montantstockgmrestant = 0
    montantstockrestant = 0

    quantitestockpm = 0
    quantitestockpmrestant = 0
    casierstockpm = 0
    casierstockpmrestant = 0
    montantstockpm = 0
    montantstockpmrestant = 0

    """ GRAND MODEL """

    quantitestockbeaufort = 0
    quantitestockrestantbeaufort = 0
    casierstockbeaufort = 0
    casierstockrestantbeaufort = 0
    montantstockbeaufort = 0
    montantstockrestantbeaufort = 0

    quantitestockawouyo = 0
    quantitestockrestantawouyo = 0
    casierstockawouyo = 0
    casierstockrestantawouyo = 0
    montantstockawouyo = 0
    montantstockrestantawouyo = 0

    quantitestockcoca = 0
    quantitestockrestantcoca = 0
    casierstockcoca = 0
    casierstockrestantcoca = 0
    montantstockcoca = 0
    montantstockrestantcoca = 0

    quantitestockfanta = 0
    quantitestockrestantfanta = 0
    casierstockfanta = 0
    casierstockrestantfanta = 0
    montantstockfanta = 0
    montantstockrestantfanta = 0

    quantitestocklager = 0
    quantitestockrestantlager = 0
    casierstocklager = 0
    casierstockrestantlager = 0
    montantstocklager = 0
    montantstockrestantlager = 0

    """ PETIT MODEL """

    quantitestockbeaufortpm = 0
    quantitestockrestantbeaufortpm = 0
    casierstockbeaufortpm = 0
    casierstockrestantbeaufortpm = 0
    montantstockbeaufortpm = 0
    montantstockrestantbeaufortpm = 0

    quantitestockawouyopm = 0
    quantitestockrestantawouyopm = 0
    casierstockawouyopm = 0
    casierstockrestantawouyopm = 0
    montantstockawouyopm = 0
    montantstockrestantawouyopm = 0

    quantitestockcocapm = 0
    quantitestockrestantcocapm = 0
    casierstockcocapm = 0
    casierstockrestantcocapm = 0
    montantstockcocapm = 0
    montantstockrestantcocapm = 0

    quantitestockfantapm = 0
    quantitestockrestantfantapm = 0
    casierstockfantapm = 0
    casierstockrestantfantapm = 0
    montantstockfantapm = 0
    montantstockrestantfantapm = 0

    quantitestocklagerpm = 0
    quantitestockrestantlagerpm = 0
    casierstocklagerpm = 0
    casierstockrestantlagerpm = 0
    montantstocklagerpm = 0
    montantstockrestantlagerpm = 0

    stocks = DepotStockProduit.objects.filter(site=gerant_site, etatdepotstockproduit=False)

    stocks_gm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "GM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)

    stocks_pm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "PM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)

    for depot in stocks:
        quantitestock += depot.quantitedepotstockproduit
        quantitestockrestant += depot.quantiterestantdepotstockproduit
        montantstock += depot.montantdepotstockproduit
        montantstockrestant += depot.montantrestantdepotstockproduit
        casierstock += depot.nombrecasierequivalentdepotstockproduit
        casierstockrestant += depot.nombrecasierequivalentrestantdepotstockproduit

    for depotgm in stocks_gm:
        quantitestockgm += depotgm.quantitedepotstockproduit
        quantitestockgmrestant += depotgm.quantiterestantdepotstockproduit
        montantstockgm += depotgm.montantdepotstockproduit
        montantstockgmrestant += depotgm.montantrestantdepotstockproduit
        casierstockgm += depotgm.nombrecasierequivalentdepotstockproduit
        casierstockgmrestant += depotgm.nombrecasierequivalentrestantdepotstockproduit

    for depotpm in stocks_pm:
        quantitestockpm += depotpm.quantitedepotstockproduit
        quantitestockpmrestant += depotpm.quantiterestantdepotstockproduit
        montantstockpm += depotpm.montantdepotstockproduit
        montantstockpmrestant += depotpm.montantrestantdepotstockproduit
        casierstockpm += depotpm.nombrecasierequivalentdepotstockproduit
        casierstockpmrestant += depotpm.nombrecasierequivalentrestantdepotstockproduit

    ####################################################################################################
    """ LES PRODUITS GRANDS MODEL """

    # GRAND MODEL : BEAUFORT
    beaufort = get_object_or_404(Produit, formatproduit="GM", libelleproduit="BEAUFORT")
    beaufort_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufort,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_beaufort in beaufort_stock:
        quantitestockbeaufort += depot_beaufort.quantitedepotstockproduit
        quantitestockrestantbeaufort += depot_beaufort.quantiterestantdepotstockproduit
        montantstockbeaufort += depot_beaufort.montantdepotstockproduit
        montantstockrestantbeaufort += depot_beaufort.montantrestantdepotstockproduit
        casierstockbeaufort += depot_beaufort.nombrecasierequivalentdepotstockproduit
        casierstockrestantbeaufort += depot_beaufort.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # GRAND MODEL : AWOUYO
    awouyo = get_object_or_404(Produit, formatproduit="GM", libelleproduit="AWOUYO")
    awouyo_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyo,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_awouyo in awouyo_stock:
        quantitestockawouyo += depot_awouyo.quantitedepotstockproduit
        quantitestockrestantawouyo += depot_awouyo.quantiterestantdepotstockproduit
        montantstockawouyo += depot_awouyo.montantdepotstockproduit
        montantstockrestantawouyo += depot_awouyo.montantrestantdepotstockproduit
        casierstockawouyo += depot_awouyo.nombrecasierequivalentdepotstockproduit
        casierstockrestantawouyo += depot_awouyo.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # GRAND MODEL : COCA
    coca = get_object_or_404(Produit, formatproduit="GM", libelleproduit="COCA")
    coca_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=coca,
                                                  site=gerant_site,
                                                  etatdepotstockproduit=False)

    for depot_coca in coca_stock:
        quantitestockcoca += depot_coca.quantitedepotstockproduit
        quantitestockrestantcoca += depot_coca.quantiterestantdepotstockproduit
        montantstockcoca += depot_coca.montantdepotstockproduit
        montantstockrestantcoca += depot_coca.montantrestantdepotstockproduit
        casierstockcoca += depot_coca.nombrecasierequivalentdepotstockproduit
        casierstockrestantcoca += depot_coca.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # GRAND MODEL : FANTA
    fanta = get_object_or_404(Produit, formatproduit="GM", libelleproduit="FANTA")
    fanta_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fanta,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_fanta in fanta_stock:
        quantitestockfanta += depot_fanta.quantitedepotstockproduit
        montantstockfanta += depot_fanta.montantdepotstockproduit
        casierstockfanta += depot_fanta.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfanta += depot_fanta.quantiterestantdepotstockproduit
        montantstockrestantfanta += depot_fanta.montantrestantdepotstockproduit
        casierstockrestantfanta += depot_fanta.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # GRAND MODEL : LAGER
    lager = get_object_or_404(Produit, formatproduit="GM", libelleproduit="LAGER")
    lager_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lager,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_lager in lager_stock:
        quantitestocklager += depot_lager.quantitedepotstockproduit
        montantstocklager += depot_lager.montantdepotstockproduit
        casierstocklager += depot_lager.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlager += depot_lager.quantiterestantdepotstockproduit
        montantstockrestantlager += depot_lager.montantrestantdepotstockproduit
        casierstockrestantlager += depot_lager.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    #####################################################################################################
    """ LES PRODUITS PETITS MODEL """

    # PETIT MODEL : BEAUFORT
    beaufortpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="BEAUFORT")
    beaufort_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufortpm,
                                                        site=gerant_site,
                                                        etatdepotstockproduit=False)

    for depot_beaufort_pm in beaufort_stockpm:
        quantitestockbeaufortpm += depot_beaufort_pm.quantitedepotstockproduit
        quantitestockrestantbeaufortpm += depot_beaufort_pm.quantiterestantdepotstockproduit
        montantstockbeaufortpm += depot_beaufort_pm.montantdepotstockproduit
        montantstockrestantbeaufortpm += depot_beaufort_pm.montantrestantdepotstockproduit
        casierstockbeaufortpm += depot_beaufort_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantbeaufortpm += depot_beaufort_pm.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # PETIT MODEL : AWOUYO
    awouyopm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="AWOUYO")
    awouyo_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyopm,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_awouyo_pm in awouyo_stockpm:
        quantitestockawouyopm += depot_awouyo_pm.quantitedepotstockproduit
        quantitestockrestantawouyopm += depot_awouyo_pm.quantiterestantdepotstockproduit
        montantstockawouyopm += depot_awouyo_pm.montantdepotstockproduit
        montantstockrestantawouyopm += depot_awouyo_pm.montantrestantdepotstockproduit
        casierstockawouyopm += depot_awouyo_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantawouyopm += depot_awouyo_pm.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # PETIT MODEL : COCA
    cocapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="COCA")
    coca_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=cocapm,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_coca_pm in coca_stockpm:
        quantitestockcocapm += depot_coca_pm.quantitedepotstockproduit
        quantitestockrestantcocapm += depot_coca_pm.quantiterestantdepotstockproduit
        montantstockcocapm += depot_coca_pm.montantdepotstockproduit
        montantstockrestantcocapm += depot_coca_pm.montantrestantdepotstockproduit
        casierstockcocapm += depot_coca_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantcocapm += depot_coca_pm.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # PETIT MODEL : FANTA
    fantapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="FANTA")
    fanta_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fantapm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_fanta_pm in fanta_stockpm:
        quantitestockfantapm += depot_fanta_pm.quantitedepotstockproduit
        montantstockfantapm += depot_fanta_pm.montantdepotstockproduit
        casierstockfantapm += depot_fanta_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfantapm += depot_fanta_pm.quantiterestantdepotstockproduit
        montantstockrestantfantapm += depot_fanta_pm.montantrestantdepotstockproduit
        casierstockrestantfantapm += depot_fanta_pm.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # PETIT MODEL : LAGER
    lagerpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="LAGER")
    lager_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lagerpm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_lager_pm in lager_stockpm:
        quantitestocklagerpm += depot_lager_pm.quantitedepotstockproduit
        montantstocklagerpm += depot_lager_pm.montantdepotstockproduit
        casierstocklagerpm += depot_lager_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlagerpm += depot_lager_pm.quantiterestantdepotstockproduit
        montantstockrestantlagerpm += depot_lager_pm.montantrestantdepotstockproduit
        casierstockrestantlagerpm += depot_lager_pm.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    return render(request, 'gestiondedepotapp/templates/depotstock/depotstock.html', locals())


@login_required()
def historique_des_achats(request):
    gerant = request.user
    gerant_site = get_object_or_404(Site, gerantsite=gerant)

    historique = HistoriquesDesAchats()

    if HistoriquesDesAchats.objects.all() is not None:
        historique_delete = HistoriquesDesAchats.objects.all()
        historique_delete.delete()

    if request.method == 'POST':
        a_form = HistoriquesAchatsForm(request.POST)
        if a_form.is_valid():
            system = a_form.save(commit=False)

            requete_achat = system.requete_achat
            numero_facture = system.no_facture

            historique.no_facture = numero_facture
            historique.date_achat = requete_achat
            historique.save()

            listes_des_achats_trouves = DepotStockProduit.objects.filter(no_facture=numero_facture, site=gerant_site,
                                                                         datecreationdepotstockproduit=requete_achat)
            if listes_des_achats_trouves is not None:
                historiques_des_achats = listes_des_achats_trouves
                return redirect('achats_de_requete')
            else:
                HttpResponse('PAS TROUVE')
    else:
        a_form = HistoriquesAchatsForm()

    return render(request, 'gestiondedepotapp/templates/depotstock/achat.html', locals())


@login_required()
def achats_de_requete(request):
    gerant = request.user
    gerant_site = get_object_or_404(Site, gerantsite=gerant)

    casier12bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="12",
                                   parametreprixemballage__emballage__type="BB")

    casier24bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="24",
                                   parametreprixemballage__emballage__type="BB")

    casier12snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="12",
                                    parametreprixemballage__emballage__type="SNB")

    casier24snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="24",
                                    parametreprixemballage__emballage__type="SNB")

    casier_total_emporter = casier12bb.bb_12 + casier24bb.bb_24 + casier12snb.snb_12 + casier24snb.snb_24

    casier_equivalent = get_object_or_404(Countwo, site=gerant_site)

    casier_vide = int(casier_total_emporter - casier_equivalent.total_casier)

    historique = get_object_or_404(HistoriquesDesAchats)
    numero_facture = historique.no_facture
    requete_achat = historique.date_achat

    historiques_achats = DepotStockProduit.objects.filter(no_facture=numero_facture, site=gerant_site,
                                                          datecreationdepotstockproduit=requete_achat)

    return render(request, 'gestiondedepotapp/templates/depotstock/achat_requete.html', locals())


@login_required()
def pertes(request):
    gerant_site = get_object_or_404(Site, gerantsite=request.user)
    print(gerant_site)
    depots = DepotStockProduit.objects.filter(site=gerant_site, etatdepotstockproduit=False)
    for perte in depots:
        if perte.casierperdu > 0 or perte.produitperdu > 0 or perte.casiercasse > 0 or perte.produitcasse > 0:
            perte.etat = True
            perte.save()

    pertes = DepotStockProduit.objects.filter(site=gerant_site, etatdepotstockproduit=False, etat=True)
    total = 0
    for perte in pertes:
        solde = perte.produitcasse + perte.produitperdu
        total += solde * perte.parametreprixachatstockproduit.prixparametreprixachatstockproduit
        a_payer = solde * perte.parametreprixachatstockproduit.prixparametreprixachatstockproduit

    remboursements = RemboursementPoduit.objects.filter(produit__site=gerant_site, produit__etat=True)

    return render(request, 'gestiondedepotapp/templates/depotstock/pertes.html', locals())


@login_required()
def pertesrembourser(request, id):
    gerant_site = get_object_or_404(Site, gerantsite=request.user)
    remboursement = get_object_or_404(RemboursementPoduit, id=id)
    reste = 0.00
    if request.method == "POST":
        form = RemboursementPoduitForm(request.POST, instance=remboursement)
        if form.is_valid():
            system = form.save(commit=False)

            if system.totalpayer is None:
                system.totalpayer = 0.00
                system.totalpayer += float(system.payer)
            elif system.totalpayer is not None:
                system.totalpayer += system.payer
            system.payer = 0.00

            solde = (remboursement.produit.produitcasse + remboursement.produit.produitperdu) * remboursement. \
                produit.parametreprixachatstockproduit.prixparametreprixachatstockproduit

            if solde != system.totalpayer:
                reste = solde - system.totalpayer
                print(system.totalpayer, ' et ', reste)
            elif solde == system.totalpayer:
                reste = 0
                produit = get_object_or_404(DepotStockProduit, site=gerant_site, id=system.produit.id)
                produit.etat = False
                produit.casierperdu = 0
                produit.produitcasse = 0
                produit.produitperdu = 0
                produit.casiercasse = 0
                produit.save()

            if solde == system.totalpayer:
                system.delete()
            elif solde != system.totalpayer:
                system.save()

            data['form_is_valid'] = True
            remboursements = RemboursementPoduit.objects.filter(produit__site=gerant_site)
            data['remboursement'] = render_to_string('gestiondedepotapp/templates/depotstock/listerembourser.html',
                                                     {'remboursements': remboursements, 'reste': reste})
    else:
        form = RemboursementPoduitForm(instance=remboursement)
        context = {
            'reste': reste,
            'form': form,
            'remboursement': remboursement,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/depotstock/pertesrembourser.html', context,
                                             request=request)

    return JsonResponse(data)


@login_required
def panierdepot(request):
    total = 0
    gerant_site = get_object_or_404(Site, gerantsite=request.user)
    site = gerant_site.libellesite
    site_html = gerant_site.libellesite
    paniers = PanierStockProduit.objects.filter(site=gerant_site, etatdepotstockproduit=False)

    if request.method == 'POST':
        u_form = CountForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            redirect('panierdepot')
    else:
        u_form = CountForm()

    if request.method == 'POST':
        form = PanierStockProduitForm(request.POST, initial={'site': site})
        if form.is_valid():
            systeme = form.save(commit=False)

            systeme.site = gerant_site
            produit = systeme.parametreprixachatstockproduit.id
            param_prix = get_object_or_404(ParametrePrixAchatStockProduit, id=produit)
            prix = param_prix.prixparametreprixachatstockproduit
            quantite = systeme.quantitedepotstockproduit

            formatproduit = systeme.parametreprixachatstockproduit.produit.formatproduit
            if formatproduit == "PM":
                systeme.nombrecasierequivalentdepotstockproduit = quantite / 24
            elif formatproduit == "GM":
                systeme.nombrecasierequivalentdepotstockproduit = quantite / 12

            if systeme.fournisseur.libellefournisseur == "BB":
                systeme.no_facture += '_BB'
            elif systeme.fournisseur.libellefournisseur == "SNB":
                systeme.no_facture += '_SNB'

            systeme.nombrecasierequivalentrestantdepotstockproduit = systeme.nombrecasierequivalentdepotstockproduit

            systeme.quantiterestantdepotstockproduit = systeme.quantitedepotstockproduit
            systeme.montantdepotstockproduit = float(quantite * prix)
            systeme.montantrestantdepotstockproduit = systeme.montantdepotstockproduit

            systeme.datemodificationdepotstockproduit = datetime.now()

            systeme.save()
        for panier in paniers:
            total += panier.montantdepotstockproduit

        return redirect('panierdepot')
    else:
        form = PanierStockProduitForm(initial={'site': site})

        paniers = PanierStockProduit.objects.filter(site=gerant_site, etatdepotstockproduit=False)
        for panier in paniers:
            total += panier.montantdepotstockproduit

    context = {
        'form': form,
        'u_form': u_form,
        'paniers': paniers,
    }
    return render(request, 'gestiondedepotapp/templates/depotstock/panier/panier.html', locals())


@login_required
def tabledepotstock(request):
    gerant_site = get_object_or_404(Site, gerantsite=request.user)
    tabledepotstocks = PanierStockProduit.objects.filter(etatdepotstockproduit=False,
                                                         site=gerant_site,
                                                         panierdepot=True)

    total_casiers: object = get_object_or_404(Countwo, site=gerant_site)

    counters = Count.objects.filter(etat=False)
    casier12bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="12",
                                   parametreprixemballage__emballage__type="BB")

    casier24bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="24",
                                   parametreprixemballage__emballage__type="BB")

    casier12snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="12",
                                    parametreprixemballage__emballage__type="SNB")

    casier24snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="24",
                                    parametreprixemballage__emballage__type="SNB")

    for counter in counters:
        if counter.bb_12 is not None:
            casier12bb.quantiterestantdepotstockemballage -= counter.bb_12
            if casier12bb.bb_12 is not None:
                casier12bb.bb_12 = counter.bb_12
            casier12bb.save()

        if counter.bb_24 is not None:
            casier24bb.quantiterestantdepotstockemballage -= counter.bb_24
            if casier24bb.bb_24 is not None:
                casier24bb.bb_24 = counter.bb_24
            casier24bb.save()

        if counter.snb_12 is not None:
            casier12snb.quantiterestantdepotstockemballage -= counter.snb_12
            if casier12snb.snb_12 is not None:
                casier12snb.snb_12 = counter.snb_12
            casier12snb.save()

        if counter.snb_24 is not None:
            casier24snb.quantiterestantdepotstockemballage -= counter.snb_24
            if casier24snb.snb_24 is not None:
                casier24snb.snb_24 = counter.snb_24
            casier24snb.save()

        counter.delete()

    for tabledepotstockk in tabledepotstocks:
        """ Copy all data from panier in depotstock """
        total_casiers.total_casier += tabledepotstockk.nombrecasierequivalentdepotstockproduit

        tableproduit = DepotStockProduit(site=gerant_site)

        tableproduit.no_facture = tabledepotstockk.no_facture
        tableproduit.fournisseur = tabledepotstockk.fournisseur
        tableproduit.parametreprixachatstockproduit = tabledepotstockk.parametreprixachatstockproduit
        tableproduit.quantitedepotstockproduit = tabledepotstockk.quantitedepotstockproduit
        tableproduit.site = tabledepotstockk.site
        tableproduit.montantdepotstockproduit = tabledepotstockk.montantdepotstockproduit
        tableproduit.nombrecasierequivalentdepotstockproduit = tabledepotstockk.nombrecasierequivalentdepotstockproduit
        tableproduit.quantiterestantdepotstockproduit = tabledepotstockk.quantiterestantdepotstockproduit
        tableproduit.montantrestantdepotstockproduit = tabledepotstockk.montantrestantdepotstockproduit
        tableproduit.nombrecasierequivalentrestantdepotstockproduit = tabledepotstockk. \
            nombrecasierequivalentrestantdepotstockproduit

        tableproduit.casierperdu = tabledepotstockk.casierperdu
        tableproduit.produitperdu = tabledepotstockk.produitperdu
        tableproduit.casiercasse = tabledepotstockk.casiercasse
        tableproduit.produitcasse = tabledepotstockk.produitcasse

        """ Copy all perte from panier in remboursement table"""

        if tabledepotstockk.casierperdu > 0 or tabledepotstockk.produitperdu > 0 or \
                tabledepotstockk.casiercasse > 0 or tabledepotstockk.produitcasse > 0:
            tabledepotstockk.etat = True

        tableproduit.datecreationdepotstockproduit = tabledepotstockk.datecreationdepotstockproduit
        tableproduit.datemodificationdepotstockproduit = tabledepotstockk.datemodificationdepotstockproduit
        tableproduit.etatdepotstockproduit = tabledepotstockk.etatdepotstockproduit

        remboursement = RemboursementPoduit()
        remboursement.produit = tableproduit

        tableproduit.save()
        remboursement.save()
        tabledepotstockk.delete()
        total_casiers.save()

    tabledepotstocks = DepotStockProduit.objects.filter(etatdepotstockproduit=False,
                                                        site=gerant_site)

    context = {
        'tabledepotstocks': tabledepotstocks,
    }
    return render(request, 'gestiondedepotapp/templates/depotstock/tabledepotstock/tabledepotstock.html', context)


@login_required
def ajoutdepot(request):
    gerant_site = get_object_or_404(Site, gerantsite=request.user)
    tabledepotstocks = DepotStockProduit.objects.filter(site=gerant_site, etatdepotstockproduit=False)

    context = {'tabledepotstocks': tabledepotstocks}

    if request.method == 'POST':
        form = DepotStockProduitForm(request.POST)
    else:
        form = DepotStockProduitForm()

    return save_all(request, form, 'gestiondedepotapp/templates/depotstock/tabledepotstock/ajoutdepot.html',
                    'depot', 'gestiondedepotapp/templates/depotstock/tabledepotstock/listetabledepotstock.html',
                    context)


@login_required
def modifiertabledepotstock(request, id):
    gerant_site = get_object_or_404(Site, gerantsite=request.user)
    tabledepotstocks = DepotStockProduit.objects.filter(site=gerant_site, etatdepotstockproduit=False)
    mycontext = {
        'tabledepotstocks': tabledepotstocks
    }
    depot = get_object_or_404(DepotStockProduit, id=id)
    if request.method == 'POST':
        form = DepotStockProduitForm(request.POST, instance=depot)
    else:
        form = DepotStockProduitForm(instance=depot)
    return save_all(request, form,
                    'gestiondedepotapp/templates/depotstock/tabledepotstock/modifiertabledepotstock.html',
                    'depot',
                    'gestiondedepotapp/templates/depotstock/tabledepotstock/listetabledepotstock.html', mycontext)


@login_required
def supprimertabledepotstock(request, id):
    data = dict()
    depot = get_object_or_404(DepotStockProduit, id=id)
    if request.method == "POST":
        depot.etatdepotstockproduit = True
        depot.save()
        data['form_is_valid'] = True

        gerant_site = get_object_or_404(Site, gerantsite=request.user)
        tabledepotstocks = DepotStockProduit.objects.filter(site=gerant_site, etatdepotstockproduit=False)

        data['depot'] = render_to_string('gestiondedepotapp/templates/depotstock/tabledepotstock/listetabledepotstock'
                                         '.html',
                                         {'tabledepotstocks': tabledepotstocks})
    else:
        context = {
            'depot': depot,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/depotstock/tabledepotstock'
                                             '/supprimertabledepotstock.html',
                                             context,
                                             request=request)

    return JsonResponse(data)


@login_required()
def petitmodel(request):
    gerant = request.user
    gerant_site = get_object_or_404(Site, gerantsite=gerant)

    quantitestockpm = 0
    quantitestockpmrestant = 0
    casierstockpm = 0
    casierstockpmrestant = 0
    montantstockpm = 0
    montantstockpmrestant = 0

    """ PETIT MODEL """

    quantitestockbeaufortpm = 0
    quantitestockrestantbeaufortpm = 0
    casierstockbeaufortpm = 0
    casierstockrestantbeaufortpm = 0
    montantstockbeaufortpm = 0
    montantstockrestantbeaufortpm = 0

    quantitestockawouyopm = 0
    quantitestockrestantawouyopm = 0
    casierstockawouyopm = 0
    casierstockrestantawouyopm = 0
    montantstockawouyopm = 0
    montantstockrestantawouyopm = 0

    quantitestockcocapm = 0
    quantitestockrestantcocapm = 0
    casierstockcocapm = 0
    casierstockrestantcocapm = 0
    montantstockcocapm = 0
    montantstockrestantcocapm = 0

    quantitestockfantapm = 0
    quantitestockrestantfantapm = 0
    casierstockfantapm = 0
    casierstockrestantfantapm = 0
    montantstockfantapm = 0
    montantstockrestantfantapm = 0

    quantitestocklagerpm = 0
    quantitestockrestantlagerpm = 0
    casierstocklagerpm = 0
    casierstockrestantlagerpm = 0
    montantstocklagerpm = 0
    montantstockrestantlagerpm = 0

    stocks_pm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "PM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)
    for depotpm in stocks_pm:
        quantitestockpm += depotpm.quantitedepotstockproduit
        quantitestockpmrestant += depotpm.quantiterestantdepotstockproduit
        montantstockpm += depotpm.montantdepotstockproduit
        montantstockpmrestant += depotpm.montantrestantdepotstockproduit
        casierstockpm += depotpm.nombrecasierequivalentdepotstockproduit
        casierstockpmrestant += depotpm.nombrecasierequivalentrestantdepotstockproduit

    """ LES PRODUITS PETITS MODEL """

    # PETIT MODEL : BEAUFORT
    beaufortpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="BEAUFORT")
    beaufort_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufortpm,
                                                        site=gerant_site,
                                                        etatdepotstockproduit=False)

    for depot_beaufort_pm in beaufort_stockpm:
        quantitestockbeaufortpm += depot_beaufort_pm.quantitedepotstockproduit
        montantstockbeaufortpm += depot_beaufort_pm.montantdepotstockproduit
        casierstockbeaufortpm += depot_beaufort_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantbeaufortpm += depot_beaufort_pm.quantiterestantdepotstockproduit
        montantstockrestantbeaufortpm += depot_beaufort_pm.montantrestantdepotstockproduit
        casierstockrestantbeaufortpm += depot_beaufort_pm.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # PETIT MODEL : AWOUYO
    awouyopm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="AWOUYO")
    awouyo_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyopm,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_awouyo_pm in awouyo_stockpm:
        quantitestockawouyopm += depot_awouyo_pm.quantitedepotstockproduit
        montantstockawouyopm += depot_awouyo_pm.montantdepotstockproduit
        casierstockawouyopm += depot_awouyo_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantawouyopm += depot_awouyo_pm.quantiterestantdepotstockproduit
        montantstockrestantawouyopm += depot_awouyo_pm.montantrestantdepotstockproduit
        casierstockrestantawouyopm += depot_awouyo_pm.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # PETIT MODEL : COCA
    cocapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="COCA")
    coca_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=cocapm,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_coca_pm in coca_stockpm:
        quantitestockcocapm += depot_coca_pm.quantitedepotstockproduit
        quantitestockrestantcocapm += depot_coca_pm.quantiterestantdepotstockproduit
        montantstockcocapm += depot_coca_pm.montantdepotstockproduit
        montantstockrestantcocapm += depot_coca_pm.montantrestantdepotstockproduit
        casierstockcocapm += depot_coca_pm.nombrecasierequivalentdepotstockproduit
        casierstockrestantcocapm += depot_coca_pm.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # PETIT MODEL : FANTA
    fantapm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="FANTA")
    fanta_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fantapm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_fanta_pm in fanta_stockpm:
        quantitestockfantapm += depot_fanta_pm.quantitedepotstockproduit
        montantstockfantapm += depot_fanta_pm.montantdepotstockproduit
        casierstockfantapm += depot_fanta_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfantapm += depot_fanta_pm.quantiterestantdepotstockproduit
        montantstockrestantfantapm += depot_fanta_pm.montantrestantdepotstockproduit
        casierstockrestantfantapm += depot_fanta_pm.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # PETIT MODEL : LAGER
    lagerpm = get_object_or_404(Produit, formatproduit="PM", libelleproduit="LAGER")
    lager_stockpm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lagerpm,
                                                     site=gerant_site,
                                                     etatdepotstockproduit=False)

    for depot_lager_pm in lager_stockpm:
        quantitestocklagerpm += depot_lager_pm.quantitedepotstockproduit
        montantstocklagerpm += depot_lager_pm.montantdepotstockproduit
        casierstocklagerpm += depot_lager_pm.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlagerpm += depot_lager_pm.quantiterestantdepotstockproduit
        montantstockrestantlagerpm += depot_lager_pm.montantrestantdepotstockproduit
        casierstockrestantlagerpm += depot_lager_pm.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    return render(request, 'gestiondedepotapp/templates/depotstock/petitmodel.html', locals())


@login_required()
def grandmodel(request):
    gerant = request.user
    gerant_site = get_object_or_404(Site, gerantsite=gerant)

    quantitestockgm = 0
    quantitestockgmrestant = 0
    casierstockgm = 0
    casierstockgmrestant = 0
    montantstockgm = 0
    montantstockgmrestant = 0
    montantstockrestant = 0

    """ GRAND MODEL """

    quantitestockbeaufort = 0
    quantitestockrestantbeaufort = 0
    casierstockbeaufort = 0
    casierstockrestantbeaufort = 0
    montantstockbeaufort = 0
    montantstockrestantbeaufort = 0

    quantitestockawouyo = 0
    quantitestockrestantawouyo = 0
    casierstockawouyo = 0
    casierstockrestantawouyo = 0
    montantstockawouyo = 0
    montantstockrestantawouyo = 0

    quantitestockcoca = 0
    quantitestockrestantcoca = 0
    casierstockcoca = 0
    casierstockrestantcoca = 0
    montantstockcoca = 0
    montantstockrestantcoca = 0

    quantitestockfanta = 0
    quantitestockrestantfanta = 0
    casierstockfanta = 0
    casierstockrestantfanta = 0
    montantstockfanta = 0
    montantstockrestantfanta = 0

    quantitestocklager = 0
    quantitestockrestantlager = 0
    casierstocklager = 0
    casierstockrestantlager = 0
    montantstocklager = 0
    montantstockrestantlager = 0

    stocks_gm = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit__formatproduit=
                                                 "GM",
                                                 site=gerant_site,
                                                 etatdepotstockproduit=False)

    for depotgm in stocks_gm:
        quantitestockgm += depotgm.quantitedepotstockproduit
        quantitestockgmrestant += depotgm.quantiterestantdepotstockproduit
        montantstockgm += depotgm.montantdepotstockproduit
        montantstockgmrestant += depotgm.montantrestantdepotstockproduit
        casierstockgm += depotgm.nombrecasierequivalentdepotstockproduit
        casierstockgmrestant += depotgm.nombrecasierequivalentrestantdepotstockproduit

    """ LES PRODUITS GRANDS MODEL """

    # GRAND MODEL : BEAUFORT
    beaufort = get_object_or_404(Produit, formatproduit="GM", libelleproduit="BEAUFORT")
    beaufort_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=beaufort,
                                                      site=gerant_site,
                                                      etatdepotstockproduit=False)

    for depot_beaufort in beaufort_stock:
        quantitestockbeaufort += depot_beaufort.quantitedepotstockproduit
        quantitestockrestantbeaufort += depot_beaufort.quantiterestantdepotstockproduit
        montantstockbeaufort += depot_beaufort.montantdepotstockproduit
        montantstockrestantbeaufort += depot_beaufort.montantrestantdepotstockproduit
        casierstockbeaufort += depot_beaufort.nombrecasierequivalentdepotstockproduit
        casierstockrestantbeaufort += depot_beaufort.nombrecasierequivalentrestantdepotstockproduit
    # END BEAUFORT

    # GRAND MODEL : AWOUYO
    awouyo = get_object_or_404(Produit, formatproduit="GM", libelleproduit="AWOUYO")
    awouyo_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=awouyo,
                                                    site=gerant_site,
                                                    etatdepotstockproduit=False)

    for depot_awouyo in awouyo_stock:
        quantitestockawouyo += depot_awouyo.quantitedepotstockproduit
        quantitestockrestantawouyo += depot_awouyo.quantiterestantdepotstockproduit
        montantstockawouyo += depot_awouyo.montantdepotstockproduit
        montantstockrestantawouyo += depot_awouyo.montantrestantdepotstockproduit
        casierstockawouyo += depot_awouyo.nombrecasierequivalentdepotstockproduit
        casierstockrestantawouyo += depot_awouyo.nombrecasierequivalentrestantdepotstockproduit
    # END AWOUYO

    # GRAND MODEL : COCA
    coca = get_object_or_404(Produit, formatproduit="GM", libelleproduit="COCA")
    coca_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=coca,
                                                  site=gerant_site,
                                                  etatdepotstockproduit=False)

    for depot_coca in coca_stock:
        quantitestockcoca += depot_coca.quantitedepotstockproduit
        quantitestockrestantcoca += depot_coca.quantiterestantdepotstockproduit
        montantstockcoca += depot_coca.montantdepotstockproduit
        montantstockrestantcoca += depot_coca.montantrestantdepotstockproduit
        casierstockcoca += depot_coca.nombrecasierequivalentdepotstockproduit
        casierstockrestantcoca += depot_coca.nombrecasierequivalentrestantdepotstockproduit
    # END COCA

    # PETIT MODEL : FANTA
    fanta = get_object_or_404(Produit, formatproduit="GM", libelleproduit="FANTA")
    fanta_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=fanta,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_fanta in fanta_stock:
        quantitestockfanta += depot_fanta.quantitedepotstockproduit
        montantstockfanta += depot_fanta.montantdepotstockproduit
        casierstockfanta += depot_fanta.nombrecasierequivalentdepotstockproduit
        quantitestockrestantfanta += depot_fanta.quantiterestantdepotstockproduit
        montantstockrestantfanta += depot_fanta.montantrestantdepotstockproduit
        casierstockrestantfanta += depot_fanta.nombrecasierequivalentrestantdepotstockproduit
    # END FANTA

    # PETIT MODEL : LAGER
    lager = get_object_or_404(Produit, formatproduit="GM", libelleproduit="LAGER")
    lager_stock = DepotStockProduit.objects.filter(parametreprixachatstockproduit__produit=lager,
                                                   site=gerant_site,
                                                   etatdepotstockproduit=False)

    for depot_lager in lager_stock:
        quantitestocklager += depot_lager.quantitedepotstockproduit
        montantstocklager += depot_lager.montantdepotstockproduit
        casierstocklager += depot_lager.nombrecasierequivalentdepotstockproduit
        quantitestockrestantlager += depot_lager.quantiterestantdepotstockproduit
        montantstockrestantlager += depot_lager.montantrestantdepotstockproduit
        casierstockrestantlager += depot_lager.nombrecasierequivalentrestantdepotstockproduit
    # END LAGER

    return render(request, 'gestiondedepotapp/templates/depotstock/grandmodele.html', locals())


@login_required
def emballage(request):
    gerant_site = get_object_or_404(Site, gerantsite=request.user)

    casier12bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="12",
                                   parametreprixemballage__emballage__type="BB")
    if casier12bb is not None:
        restant12bb = casier12bb.quantitedepotstockemballage - casier12bb.quantiterestantdepotstockemballage

    casier24bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="24",
                                   parametreprixemballage__emballage__type="BB")
    if casier24bb is not None:
        restant24bb = casier24bb.quantitedepotstockemballage - casier24bb.quantiterestantdepotstockemballage

    casier12snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="12",
                                    parametreprixemballage__emballage__type="SNB")
    if casier12snb is not None:
        restant12snb = casier12snb.quantitedepotstockemballage - casier12snb.quantiterestantdepotstockemballage

    casier24snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="24",
                                    parametreprixemballage__emballage__type="SNB")
    if casier24snb is not None:
        restant24snb = casier24snb.quantitedepotstockemballage - casier24snb.quantiterestantdepotstockemballage

    return render(request, 'gestiondedepotapp/templates/emballage/emballage.html', locals())


@login_required
def embal(request):
    embals = Emballage.objects.filter(etatemballage=False)
    context = {
        'embals': embals,
    }
    return render(request, 'gestiondedepotapp/templates/embal/embal.html',
                  context)


@login_required
def ajouterembal(request):
    embals = Emballage.objects.filter(etatemballage=False)

    context = {'embals': embals}

    if request.method == 'POST':
        form = EmballageForm(request.POST)
    else:
        form = EmballageForm()

    return save_all(request, form, 'gestiondedepotapp/templates/embal/ajouterembal.html', 'embal',
                    'gestiondedepotapp/templates/embal/listeembal.html', context)


@login_required
def modifierembal(request, id):
    embals = Emballage.objects.filter(etatemballage=False)
    mycontext = {
        'embals': embals
    }
    embal = get_object_or_404(Emballage, id=id)
    if request.method == 'POST':
        form = EmballageForm(request.POST, instance=embal)
    else:
        form = EmballageForm(instance=embal)
    return save_all(request, form, 'gestiondedepotapp/templates/embal/modifierembal.html', 'embal',
                    'gestiondedepotapp/templates/embal/listeembal.html', mycontext)


@login_required
def supprimerembal(request, id):
    data = dict()
    embal = get_object_or_404(Emballage, id=id)
    if request.method == "POST":
        embal.etatemballage = True
        embal.save()
        data['form_is_valid'] = True
        embals = Emballage.objects.filter(etatemballage=False)
        data['embal'] = render_to_string('gestiondedepotapp/templates/embal/listeembal.html',
                                         {'embals': embals})
    else:
        context = {
            'embal': embal,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/embal/supprimerembal.html', context,
                                             request=request)

    return JsonResponse(data)


@login_required
def paramembal(request):
    paramembals = ParametrePrixEmballage.objects.filter(etatparametreprixemballage=False)
    context = {
        'paramembals': paramembals,
    }
    return render(request, 'gestiondedepotapp/templates/emballage/tableemballagestock/paramembal/paramembal.html',
                  context)


@login_required
def ajouterparamembal(request):
    paramembals = ParametrePrixEmballage.objects.filter(etatparametreprixemballage=False)

    context = {'paramembals': paramembals}

    if request.method == 'POST':
        form = ParametrePrixEmballageForm(request.POST)
    else:
        form = ParametrePrixEmballageForm()

    return save_all(request, form, 'gestiondedepotapp/templates/emballage/tableemballagestock/paramembal'
                                   '/ajouterparamembal.html', 'paramembal',
                    'gestiondedepotapp/templates/emballage/tableemballagestock/paramembal'
                    '/listeparamprixemballage.html', context)


@login_required
def modifierparamembal(request, id):
    paramembals = ParametrePrixEmballage.objects.filter(etatparametreprixemballage=False)
    mycontext = {
        'paramembals': paramembals
    }
    paramembal = get_object_or_404(ParametrePrixEmballage, id=id)
    if request.method == 'POST':
        form = ParametrePrixEmballageForm(request.POST, instance=paramembal)
    else:
        form = ParametrePrixEmballageForm(instance=paramembal)
    return save_all(request, form, 'gestiondedepotapp/templates/emballage/tableemballagestock/paramembal'
                                   '/modifierparamembal.html', 'paramembal',
                    'gestiondedepotapp/templates/emballage/tableemballagestock/paramembal'
                    '/listeparamprixemballage.html', mycontext)


@login_required
def supprimerparamembal(request, id):
    data = dict()
    paramembal = get_object_or_404(ParametrePrixEmballage, id=id)
    if request.method == "POST":
        paramembal.etatparametreprixemballage = True
        paramembal.save()
        data['form_is_valid'] = True
        paramembals = ParametrePrixEmballage.objects.filter(etatparametreprixemballage=False)
        data['paramembal'] = render_to_string('gestiondedepotapp/templates/emballage/tableemballagestock/paramembal'
                                              '/listeparamprixemballage.html',
                                              {'paramembals': paramembals})
    else:
        context = {
            'paramembal': paramembal,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/emballage/tableemballagestock/paramembal'
                                             '/supprimerparamembal.html', context,
                                             request=request)

    return JsonResponse(data)


@login_required
def panieremaballage(request):
    gerant_site = get_object_or_404(Site, gerantsite=request.user)
    print(gerant_site)
    site = gerant_site.libellesite
    site_html = gerant_site.libellesite

    paniers = PanierEmballage.objects.filter(etatdepotstockemballage=False, site=gerant_site)

    if request.method == 'POST':
        form = PanierEmballageForm(request.POST, initial={"site": gerant_site})
        if form.is_valid():
            systeme = form.save(commit=False)

            emballage = systeme.parametreprixemballage.id
            param_prix = get_object_or_404(ParametrePrixEmballage, id=emballage)
            prix = param_prix.prixparametreprixemballage
            quantite = systeme.quantitedepotstockemballage

            systeme.site = gerant_site
            systeme.quantiterestantdepotstockemballage = systeme.quantitedepotstockemballage
            systeme.montantdepotstockemballage = float(quantite * prix)
            systeme.montantrestantdepotstockemballage = float(systeme.quantiterestantdepotstockemballage * prix)

            systeme.datemodificationdepotstockemballage = datetime.now()

            systeme.save()

            return redirect('panieremballage')
    else:
        form = PanierEmballageForm(initial={"site": gerant_site})

    context = {
        'form': form,
        'paniers': paniers,
        'site_html': site_html,
        'gerant_site': gerant_site
    }
    return render(request, 'gestiondedepotapp/templates/emballage/panier/panier.html', context)


@login_required
def tableemballagestock(request):
    gerant_site = get_object_or_404(Site, gerantsite=request.user)
    panieremballages = PanierEmballage.objects.filter(etatdepotstockemballage=False,
                                                      panieremballage=True, site=gerant_site)

    casier12bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="12",
                                   parametreprixemballage__emballage__type="BB")

    for panier in panieremballages:
        if panier.parametreprixemballage.emballage.libelleemballage == "CASIER" and \
                panier.parametreprixemballage.emballage.format == "12" and \
                panier.parametreprixemballage.emballage.type == "BB":
            casier12bb.fournisseur = panier.fournisseur
            casier12bb.parametreprixemballage = panier.parametreprixemballage

            if casier12bb.quantitedepotstockemballage is None:
                casier12bb.quantitedepotstockemballage = 0
                casier12bb.quantitedepotstockemballage += panier.quantitedepotstockemballage
            elif casier12bb.quantitedepotstockemballage is not None:
                casier12bb.quantitedepotstockemballage += panier.quantitedepotstockemballage

            if casier12bb.montantdepotstockemballage is None:
                casier12bb.montantdepotstockemballage = 0.00
                casier12bb.montantdepotstockemballage += float(panier.montantdepotstockemballage)
            elif casier12bb.montantdepotstockemballage is not None:
                casier12bb.montantdepotstockemballage += panier.montantdepotstockemballage

            if casier12bb.quantiterestantdepotstockemballage is None:
                casier12bb.quantiterestantdepotstockemballage = 0.00
                casier12bb.quantiterestantdepotstockemballage += panier.quantiterestantdepotstockemballage
            elif casier12bb.quantiterestantdepotstockemballage is not None:
                casier12bb.quantiterestantdepotstockemballage += panier.quantiterestantdepotstockemballage

            if casier12bb.montantrestantdepotstockemballage is None:
                casier12bb.montantrestantdepotstockemballage = 0.00
                casier12bb.montantrestantdepotstockemballage += float(panier.montantrestantdepotstockemballage)
            elif casier12bb.montantrestantdepotstockemballage is not None:
                casier12bb.montantrestantdepotstockemballage += panier.montantrestantdepotstockemballage

            casier12bb.datecreationdepotstockemballage = panier.datecreationdepotstockemballage
            casier12bb.datemodificationdepotstockemballage = panier.datemodificationdepotstockemballage
            casier12bb.etatdepotstockemballage = panier.etatdepotstockemballage

            casier12bb.save()

    casier24bb = get_object_or_404(TotalEmballage,
                                   site=gerant_site,
                                   etatdepotstockemballage=False,
                                   parametreprixemballage__emballage__libelleemballage="CASIER",
                                   parametreprixemballage__emballage__format="24",
                                   parametreprixemballage__emballage__type="BB")
    for panier in panieremballages:
        if panier.parametreprixemballage.emballage.libelleemballage == "CASIER" and \
                panier.parametreprixemballage.emballage.format == "24" and \
                panier.parametreprixemballage.emballage.type == "BB":
            casier24bb.fournisseur = panier.fournisseur
            casier24bb.parametreprixemballage = panier.parametreprixemballage

            if casier24bb.quantitedepotstockemballage is None:
                casier24bb.quantitedepotstockemballage = 0
                casier24bb.quantitedepotstockemballage += panier.quantitedepotstockemballage
            elif casier24bb.quantitedepotstockemballage is not None:
                casier24bb.quantitedepotstockemballage += panier.quantitedepotstockemballage

            if casier24bb.montantdepotstockemballage is None:
                casier24bb.montantdepotstockemballage = 0.00
                casier24bb.montantdepotstockemballage += float(panier.montantdepotstockemballage)
            elif casier24bb.montantdepotstockemballage is not None:
                casier24bb.montantdepotstockemballage += panier.montantdepotstockemballage

            if casier24bb.quantiterestantdepotstockemballage is None:
                casier24bb.quantiterestantdepotstockemballage = 0.00
                casier24bb.quantiterestantdepotstockemballage += panier.quantiterestantdepotstockemballage
            elif casier24bb.quantiterestantdepotstockemballage is not None:
                casier24bb.quantiterestantdepotstockemballage += panier.quantiterestantdepotstockemballage

            if casier24bb.montantrestantdepotstockemballage is None:
                casier24bb.montantrestantdepotstockemballage = 0.00
                casier24bb.montantrestantdepotstockemballage += float(panier.montantrestantdepotstockemballage)
            elif casier24bb.montantrestantdepotstockemballage is not None:
                casier24bb.montantrestantdepotstockemballage += panier.montantrestantdepotstockemballage

            casier24bb.datecreationdepotstockemballage = panier.datecreationdepotstockemballage
            casier24bb.datemodificationdepotstockemballage = panier.datemodificationdepotstockemballage
            casier24bb.etatdepotstockemballage = panier.etatdepotstockemballage

            casier24bb.save()

    casier12snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="12",
                                    parametreprixemballage__emballage__type="SNB")
    for panier in panieremballages:
        if panier.parametreprixemballage.emballage.libelleemballage == "CASIER" and \
                panier.parametreprixemballage.emballage.format == "12" and \
                panier.parametreprixemballage.emballage.type == "SNB":
            casier12snb.fournisseur = panier.fournisseur
            casier12snb.parametreprixemballage = panier.parametreprixemballage

            if casier12snb.quantitedepotstockemballage is None:
                casier12snb.quantitedepotstockemballage = 0
                casier12snb.quantitedepotstockemballage += panier.quantitedepotstockemballage
            elif casier12snb.quantitedepotstockemballage is not None:
                casier12snb.quantitedepotstockemballage += panier.quantitedepotstockemballage

            if casier12snb.montantdepotstockemballage is None:
                casier12snb.montantdepotstockemballage = 0.00
                casier12snb.montantdepotstockemballage += float(panier.montantdepotstockemballage)
            elif casier12snb.montantdepotstockemballage is not None:
                casier12snb.montantdepotstockemballage += panier.montantdepotstockemballage

            if casier12snb.quantiterestantdepotstockemballage is None:
                casier12snb.quantiterestantdepotstockemballage = 0.00
                casier12snb.quantiterestantdepotstockemballage += panier.quantiterestantdepotstockemballage
            elif casier12snb.quantiterestantdepotstockemballage is not None:
                casier12snb.quantiterestantdepotstockemballage += panier.quantiterestantdepotstockemballage

            if casier12snb.montantrestantdepotstockemballage is None:
                casier12snb.montantrestantdepotstockemballage = 0.00
                casier12snb.montantrestantdepotstockemballage += float(panier.montantrestantdepotstockemballage)
            elif casier12snb.montantrestantdepotstockemballage is not None:
                casier12snb.montantrestantdepotstockemballage += panier.montantrestantdepotstockemballage

            casier12snb.datecreationdepotstockemballage = panier.datecreationdepotstockemballage
            casier12snb.datemodificationdepotstockemballage = panier.datemodificationdepotstockemballage
            casier12snb.etatdepotstockemballage = panier.etatdepotstockemballage

            casier12snb.save()

    casier24snb = get_object_or_404(TotalEmballage,
                                    site=gerant_site,
                                    etatdepotstockemballage=False,
                                    parametreprixemballage__emballage__libelleemballage="CASIER",
                                    parametreprixemballage__emballage__format="24",
                                    parametreprixemballage__emballage__type="SNB")
    for panier in panieremballages:
        if panier.parametreprixemballage.emballage.libelleemballage == "CASIER" and \
                panier.parametreprixemballage.emballage.format == "24" and \
                panier.parametreprixemballage.emballage.type == "SNB":
            casier24snb.fournisseur = panier.fournisseur
            casier24snb.parametreprixemballage = panier.parametreprixemballage

            if casier24snb.quantitedepotstockemballage is None:
                casier24snb.quantitedepotstockemballage = 0
                casier24snb.quantitedepotstockemballage += panier.quantitedepotstockemballage
            elif casier24snb.quantitedepotstockemballage is not None:
                casier24snb.quantitedepotstockemballage += panier.quantitedepotstockemballage

            if casier24snb.montantdepotstockemballage is None:
                casier24snb.montantdepotstockemballage = 0.00
                casier24snb.montantdepotstockemballage += float(panier.montantdepotstockemballage)
            elif casier24snb.montantdepotstockemballage is not None:
                casier24snb.montantdepotstockemballage += panier.montantdepotstockemballage

            if casier24snb.quantiterestantdepotstockemballage is None:
                casier24snb.quantiterestantdepotstockemballage = 0.00
                casier24snb.quantiterestantdepotstockemballage += panier.quantiterestantdepotstockemballage
            elif casier24snb.quantiterestantdepotstockemballage is not None:
                casier24snb.quantiterestantdepotstockemballage += panier.quantiterestantdepotstockemballage

            if casier24snb.montantrestantdepotstockemballage is None:
                casier24snb.montantrestantdepotstockemballage = 0.00
                casier24snb.montantrestantdepotstockemballage += float(panier.montantrestantdepotstockemballage)
            elif casier24snb.montantrestantdepotstockemballage is not None:
                casier24snb.montantrestantdepotstockemballage += panier.montantrestantdepotstockemballage

            casier24snb.datecreationdepotstockemballage = panier.datecreationdepotstockemballage
            casier24snb.datemodificationdepotstockemballage = panier.datemodificationdepotstockemballage
            casier24snb.etatdepotstockemballage = panier.etatdepotstockemballage

            casier24snb.save()

    for panieremballage in panieremballages:
        tableemballage = DepotStockEmballage(site=gerant_site)

        tableemballage.fournisseur = panieremballage.fournisseur
        tableemballage.parametreprixemballage = panieremballage.parametreprixemballage
        tableemballage.quantitedepotstockemballage = panieremballage.quantitedepotstockemballage
        tableemballage.site = panieremballage.site
        tableemballage.montantdepotstockemballage = panieremballage.montantdepotstockemballage
        tableemballage.quantiterestantdepotstockemballage = panieremballage.quantiterestantdepotstockemballage
        tableemballage.quantiterestantdepotstockemballage = panieremballage.quantiterestantdepotstockemballage
        tableemballage.montantrestantdepotstockemballage = panieremballage.montantrestantdepotstockemballage
        tableemballage.datecreationdepotstockemballage = panieremballage.datecreationdepotstockemballage
        tableemballage.datemodificationdepotstockemballage = panieremballage.datemodificationdepotstockemballage
        tableemballage.datemodificationdepotstockemballage = panieremballage.datemodificationdepotstockemballage
        tableemballage.etatdepotstockemballage = panieremballage.etatdepotstockemballage

        tableemballage.save()
        panieremballage.delete()

    tableemballagestocks = DepotStockEmballage.objects.filter(etatdepotstockemballage=False, site=gerant_site)

    context = {
        'tableemballagestocks': tableemballagestocks,
    }
    return render(request,
                  'gestiondedepotapp/templates/emballage/tableemballagestock/tableemballagestock.html', context)


"""
GESTION DES VENTES
"""


# CLIENTS
@login_required
def client(request):
    clients = Client.objects.filter(etat=False)
    return render(request, 'gestiondedepotapp/templates/client/client.html', locals())


@login_required
def ajouterclient(request):
    clients = Client.objects.filter(etat=False)

    context = {'clients': clients}

    form = ClientForm(request.POST) if request.method == 'POST' else ClientForm()
    return save_all(request, form, 'gestiondedepotapp/templates/client/ajouterclient.html',
                    'client', 'gestiondedepotapp/templates/client/listeclient.html', context)


@login_required
def modifierclient(request, id):
    clients = Client.objects.filter(etat=False)
    mycontext = {
        'clients': clients
    }
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
    else:
        form = ClientForm(instance=client)
    return save_all(request, form, 'gestiondedepotapp/templates/client/modifierclient.html', 'client',
                    'gestiondedepotapp/templates/client/listeclient.html', mycontext)


@login_required
def supprimerclient(request, id):
    data = dict()
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        client.archive = True
        client.save()
        data['form_is_valid'] = True
        clients = Client.objects.filter(etat=False)
        data['client'] = render_to_string('gestiondedepotapp/templates/client/listeclient.html',
                                          {'clients': clients})
    else:
        context = {
            'client': client,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/client/supprimerclient.html', context,
                                             request=request)

    return JsonResponse(data)


# END CLIENT


# PARAM PRIX PRODUIT VENTE
@login_required
def paramprixvente(request):
    paramprixventes = ParamPrixProduitVente.objects.filter(etat=False)
    return render(request, 'gestiondedepotapp/templates/paramprixvente/paramprixvente.html', locals())


@login_required
def ajouterparamprixvente(request):
    paramprixventes = ParamPrixProduitVente.objects.filter(etat=False)

    context = {'paramprixventes': paramprixventes}

    if request.method == 'POST':
        form = ParamPrixProduitVenteForm(request.POST)
    else:
        form = ParamPrixProduitVenteForm()

    return save_all(request, form, 'gestiondedepotapp/templates/paramprixvente/ajouterparamprixvente.html',
                    'paramprixvente', 'gestiondedepotapp/templates/paramprixvente/listeparamprixvente.html', context)


@login_required
def modifierparamprixvente(request, id):
    paramprixventes = ParamPrixProduitVente.objects.filter(etat=False)
    mycontext = {
        'paramprixventes': paramprixventes
    }
    paramprixvente = get_object_or_404(ParamPrixProduitVente, id=id)
    if request.method == 'POST':
        form = ParamPrixProduitVenteForm(request.POST, instance=paramprixvente)
    else:
        form = ParamPrixProduitVenteForm(instance=paramprixvente)
    return save_all(request, form, 'gestiondedepotapp/templates/paramprixvente/modifierparamprixvente.html',
                    'paramprixvente', 'gestiondedepotapp/templates/paramprixvente/listeparamprixvente.html', mycontext)


@login_required
def supprimerparamprixvente(request, id):
    data = dict()
    paramprixvente = get_object_or_404(ParamPrixProduitVente, id=id)
    if request.method == "POST":
        paramprixvente.etat = True
        paramprixvente.save()
        data['form_is_valid'] = True
        paramprixventes = ParamPrixProduitVente.objects.filter(etat=False)
        data['paramprixvente'] = render_to_string('gestiondedepotapp/templates/paramprixvente/listeparamprixvente.html',
                                                  {'paramprixventes': paramprixventes})
    else:
        context = {
            'paramprixvente': paramprixvente,
        }
        data['html_form'] = render_to_string('gestiondedepotapp/templates/paramprixvente/supprimerparamprixvente.html',
                                             context, request=request)

    return JsonResponse(data)


# END PARAM PRIX PRODUIT VENTE

@login_required
def vente(request):
    return render(request, 'gestiondedepotapp/templates/vente/vente.html', locals())


@login_required
def paniervente(request):
    total = 0
    totalarrondi = 0
    parrondi = 0
    gerant_site = get_object_or_404(Site, gerantsite=request.user)
    site = gerant_site.libellesite
    site_html = gerant_site.libellesite
    paniers = PanierVente.objects.filter(site=gerant_site, etat=False)
    print(paniers.values())

    if request.method == 'POST':
        form = PanierVenteForm(request.POST, initial={'site': site})
        if form.is_valid():
            systeme = form.save(commit=False)

            produit = systeme.paramprixproduitvente.id
            param_prix = get_object_or_404(ParamPrixProduitVente, id=produit)
            prixreelle = param_prix.prixreelle
            parrondi = param_prix.prixarrondi
            quantite = systeme.quantitevendu

            systeme.site = gerant_site
            systeme.montantvendu = float(quantite * prixreelle)
            systeme.montantarrondi = float(quantite * parrondi)

            if systeme.paramprixproduitvente.produit.formatproduit == "GM":
                systeme.casier = quantite / 12
            elif systeme.paramprixproduitvente.produit.formatproduit == "PM":
                systeme.casier = quantite / 24

            systeme.datemodification = datetime.now()

            systeme.save()

        for panier in paniers:
            total += panier.montantvendu
            totalarrondi += panier.montantarrondi
        return redirect('paniervente')

    else:
        form = PanierVenteForm(initial={'site': site})

        paniers = PanierVente.objects.filter(site=gerant_site, etat=False)
        for panier in paniers:
            total += panier.montantvendu
            totalarrondi += panier.montantarrondi

    context = {
        'form': form,
        'paniers': paniers,
    }
    return render(request, 'gestiondedepotapp/templates/vente/panier.html', locals())


def embalconsigne(request):
    return render(request, 'gestiondedepotapp/templates/embalconsigne/embalconsigne.html', locals())


def depot(request):
    depots = DepotStockProduit.objects.filter(etatdepotstockproduit=False).order_by('id')
    for dpt in depots:
        if dpt.parametreprixachatstockproduit.produit.libelleproduit == 'LAGER' \
                and dpt.parametreprixachatstockproduit.produit.formatproduit == 'GM':
            pass
    return render(request, 'gestiondedepotapp/templates/depot.html', locals())
