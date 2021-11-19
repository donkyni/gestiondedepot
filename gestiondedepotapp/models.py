from django.contrib.auth import models as auth_models
from django.db import models


class CategorieProduit(models.Model):
    libellecategorieproduit = models.CharField(max_length=100, null=True, verbose_name='Catégorie')

    # variables systemes
    datecreationcategorieproduit = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationcategorieproduit = models.DateTimeField(auto_now_add=True, null=True)
    etatcategorieproduit = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.libellecategorieproduit

    class Meta:
        ordering = ('-id',)


class Produit(models.Model):
    format = (
        (u"PM", u"PM"),
        (u"GM", u"GM")
    )

    libelleproduit = models.CharField(max_length=100, null=True)
    formatproduit = models.CharField(choices=format, max_length=100, null=True)
    contenanceproduit = models.IntegerField(null=True)
    categorieproduit = models.ForeignKey(CategorieProduit, on_delete=models.SET_NULL, null=True)

    # variables systemes
    datecreationproduit = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationproduit = models.DateTimeField(auto_now_add=True, null=True)
    etatproduit = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.libelleproduit + ' ' + self.formatproduit

    class Meta:
        ordering = ('-id',)


class ParametrePrixAchatStockProduit(models.Model):
    DETAILSPRIXPRODUIT = (
        (u'Casier entier', u'Casier entier'),
        (u'Trois-quart de casier', u'Trois-quart de casier'),
        (u'Démi-casier', u'Démi-asier '),
        (u'Quart de casier', u'Quart de casier'),
    )
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    detailprixproduit = models.CharField(choices=DETAILSPRIXPRODUIT, max_length=25, null=True)
    prixparametreprixachatstockproduit = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    # variables systemes
    datecreationparametreprixachatstockproduit = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationparametreprixachatstockproduit = models.DateTimeField(auto_now_add=True, null=True)
    etatparametreprixachatstockproduit = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.produit) + ': ' + \
               str(self.detailprixproduit) + ' ---> ' + \
               str(self.prixparametreprixachatstockproduit)

    class Meta:
        ordering = ('-id',)


class UserManager(auth_models.BaseUserManager):

    def create_user(self, pseudo, adresse, nom, prenom, password=None):
        if not pseudo:
            raise ValueError('Users must have an telephone number')
        user = self.model(pseudo=pseudo)
        user.adresse = adresse
        user.nom = nom
        user.prenom = prenom
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, pseudo, adresse, nom, prenom, password):
        user = self.create_user(
            pseudo,
            adresse=adresse,
            nom=nom,
            prenom=prenom,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Droits(models.Model):
    nom_du_droit = models.CharField(max_length=255)
    archive = models.BooleanField(default=False, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom_du_droit

    class Meta:
        ordering = ('-id',)
        verbose_name = "Droits"
        verbose_name_plural = "Droits"


class Profils(models.Model):
    nom = models.CharField(max_length=255, null=True)
    archive = models.BooleanField(default=False, null=True)
    droits = models.ManyToManyField(Droits, through="DroitsProfils")
    date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ('-id',)
        verbose_name = "Profil"
        verbose_name_plural = "Profil"


class DroitsProfils(models.Model):
    profil = models.ForeignKey(Profils, on_delete=models.SET_NULL, null=True)
    droit = models.ForeignKey(Droits, on_delete=models.SET_NULL, null=True)
    ecriture = models.BooleanField(default=False, null=True)
    lecture = models.BooleanField(default=False, null=True)
    modification = models.BooleanField(default=False, null=True)
    suppression = models.BooleanField(default=False, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = "Droits profils"
        verbose_name_plural = "Droits profils"


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    SEXE = (
        (u"Homme", u"Homme"),
        (u"Femme", u"Femme")
    )

    """
    Informations de base
    """
    pseudo = models.CharField(unique=True, max_length=255, null=True, blank=False,
                              help_text="Le nom d'utilisateur servira à se connecter à la plateforme")
    nom = models.CharField(max_length=255, null=True)
    prenom = models.CharField(max_length=255, blank=False, null=True)
    adresse = models.CharField(max_length=255, null=True, blank=False)
    telephone = models.BigIntegerField(blank=False, null=True, unique=True)
    profil = models.ForeignKey(Profils, on_delete=models.SET_NULL, null=True)

    """
    Informations supplémentaires
    """
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars")
    sexe = models.CharField(choices=SEXE, max_length=120, null=True, blank=True, )

    """
    Données systèmes
    """

    """
    Django settings
    """
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_d_ajout = models.DateTimeField(auto_now_add=True, null=True,
                                        verbose_name="Date d'enrégistrement de l'utilisateur")

    objects = UserManager()

    USERNAME_FIELD = 'pseudo'
    REQUIRED_FIELDS = ['nom', 'prenom', 'adresse']

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateur'
        ordering = ('-id',)

    def __str__(self):
        return self.nom + ' ' + self.prenom

    def has_perm(self, perm, obj=None):
        """Does the utilisateur have a specific permission?"""
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        """Does the utilisateur have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return self.is_admin

    @property
    def is_staff(self):
        """Is the utilisateur a member of staff?"""
        # Réponse la plus simple possible : Tous les administrateurs sont du personnel
        return self.is_active

    def __unicode__(self):
        # pass
        return u'{0}'.format(self.get_full_name())

    def get_short_name(self):
        # pass
        return self.nom

    def get_full_name(self):
        # pass
        return u'{0} {1}'.format(self.nom, self.prenom)


class Site(models.Model):
    libellesite = models.CharField(max_length=255, null=True)
    adressesite = models.CharField(max_length=255, null=True)
    gerantsite = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # variables systemes
    datecreationsite = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationsite = models.DateTimeField(auto_now_add=True, null=True)
    etatsite = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.libellesite

    class Meta:
        ordering = ('id',)


class Fournisseur(models.Model):
    libellefournisseur = models.CharField(max_length=100, null=True, blank=True)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True, blank=True)
    adressefournisseur = models.CharField(max_length=100, null=True)
    telephonefournisseur = models.CharField(max_length=25, null=True)

    # variables systemes
    datecreationfournisseur = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationfournisseur = models.DateTimeField(auto_now_add=True, null=True)
    etatfournisseur = models.BooleanField(default=False, null=True)

    def __str__(self):
        if self.libellefournisseur:
            return self.libellefournisseur
        elif str(self.site):
            return str(self.site)

    class Meta:
        ordering = ('id',)


class Emballage(models.Model):
    format = (
        (u"12", u"12"),
        (u"24", u"24")
    )
    type = (
        (u"SNB", u"SNB"),
        (u"BB", u"BB")
    )
    libelleemballage = models.CharField(null=True, max_length=255, verbose_name='Libelle de l\'emballage')
    format = models.CharField(choices=format, max_length=7, null=True)
    type = models.CharField(choices=type, max_length=8, null=True)

    # variables systemes
    datecreationemballage = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationemballage = models.DateTimeField(auto_now_add=True, null=True)
    etatemballage = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.libelleemballage + ' ' + self.format + ' ' + self.type

    class Meta:
        ordering = ('-id',)


class ParametrePrixEmballage(models.Model):
    emballage = models.ForeignKey(Emballage, on_delete=models.SET_NULL, null=True)
    prixparametreprixemballage = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    # variables systemes
    datecreationparametreprixemballage = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationparametreprixemballage = models.DateTimeField(auto_now_add=True, null=True)
    etatparametreprixemballage = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.emballage) + ' ---> ' + str(self.prixparametreprixemballage)

    class Meta:
        ordering = ('-id',)


class DepotStockEmballage(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True)
    parametreprixemballage = models.ForeignKey(ParametrePrixEmballage,
                                               on_delete=models.SET_NULL,
                                               null=True,
                                               blank=True,
                                               verbose_name='Prix d\'Emballage')
    quantitedepotstockemballage = models.IntegerField(null=True)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)

    # paramètres systèmes
    montantdepotstockemballage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantiterestantdepotstockemballage = models.IntegerField(null=True, blank=True)
    montantrestantdepotstockemballage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # variables systemes
    datecreationdepotstockemballage = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationdepotstockemballage = models.DateTimeField(auto_now_add=True, null=True)
    etatdepotstockemballage = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.parametreprixemballage)

    class Meta:
        ordering = ('-id',)


class PanierEmballage(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True)
    parametreprixemballage = models.ForeignKey(ParametrePrixEmballage,
                                               on_delete=models.SET_NULL,
                                               null=True,
                                               verbose_name='Prix d\'Emballage')
    quantitedepotstockemballage = models.IntegerField(null=True)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)

    # paramètres systèmes
    montantdepotstockemballage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantiterestantdepotstockemballage = models.IntegerField(null=True, blank=True)
    montantrestantdepotstockemballage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # variables systemes
    panieremballage = models.BooleanField(default=True, null=True)
    datecreationdepotstockemballage = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationdepotstockemballage = models.DateTimeField(auto_now_add=True, null=True)
    etatdepotstockemballage = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.parametreprixemballage)

    class Meta:
        ordering = ('id',)


class Count(models.Model):
    # variables servant à decrementer le nombre total de casier
    bb_12 = models.IntegerField(null=True, blank=True, verbose_name="Total casier de 12 BB empoter pour l'achat",
                                help_text="Entrer le nombre total de casier de 12 BB emporter pour l'achat")
    bb_24 = models.IntegerField(null=True, blank=True, verbose_name="Total casier de 24 BB empoter pour l'achat",
                                help_text="Entrer le nombre total de casier de 24 BB emporter pour l'achat")
    snb_12 = models.IntegerField(null=True, blank=True, verbose_name="Total casier de 12 SNB empoter pour l'achat",
                                 help_text="Entrer le nombre total de casier de 12 SNB emporter pour l'achat")
    snb_24 = models.IntegerField(null=True, blank=True, verbose_name="Total casier de 24 SNB empoter pour l'achat",
                                 help_text="Entrer le nombre total de casier de 24 SNB emporter pour l'achat")
    etat = models.BooleanField(default=False, null=True)


class Countwo(models.Model):
    # variables servant à decrementer le nombre total de casier par site
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True, blank=True)
    total_casier = models.IntegerField(null=True, blank=True, verbose_name="Total casier")
    ancien = models.IntegerField(null=True, blank=True, verbose_name="Ancien total casier")


class TotalEmballage(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True, blank=True, )
    parametreprixemballage = models.ForeignKey(ParametrePrixEmballage,
                                               on_delete=models.SET_NULL,
                                               null=True,
                                               blank=True,
                                               verbose_name='Prix d\'Emballage')
    quantitedepotstockemballage = models.IntegerField(null=True, blank=True, )
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)

    # paramètres systèmes
    montantdepotstockemballage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantiterestantdepotstockemballage = models.IntegerField(null=True, blank=True)
    montantrestantdepotstockemballage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    bb_12 = models.IntegerField(null=True, default=0)
    bb_24 = models.IntegerField(null=True, default=0)
    snb_12 = models.IntegerField(null=True, default=0)
    snb_24 = models.IntegerField(null=True, default=0)

    # variables systemes
    datecreationdepotstockemballage = models.DateTimeField(auto_now_add=True, null=True)
    datemodificationdepotstockemballage = models.DateTimeField(auto_now_add=True, null=True)
    etatdepotstockemballage = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.parametreprixemballage)

    class Meta:
        ordering = ('-id',)


class DepotStockProduit(models.Model):
    no_facture = models.CharField(max_length=15, null=True, blank=True, verbose_name='Numéro de facture')
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True)
    parametreprixachatstockproduit = models.ForeignKey(ParametrePrixAchatStockProduit,
                                                       on_delete=models.SET_NULL,
                                                       null=True,
                                                       verbose_name='Produit prix')
    quantitedepotstockproduit = models.IntegerField(null=True, blank=False)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)

    # parametres systemes
    montantdepotstockproduit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nombrecasierequivalentdepotstockproduit = models.IntegerField(null=True, blank=True,
                                                                  help_text="24 bouteilles pour petit model et 12 "
                                                                            "bouteilles pour grand model")
    quantiterestantdepotstockproduit = models.IntegerField(null=True, blank=True)
    montantrestantdepotstockproduit = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                                          blank=True)
    nombrecasierequivalentrestantdepotstockproduit = models.IntegerField(null=True, blank=True,
                                                                         help_text="24 bouteilles pour petit model et "
                                                                                   "12 bouteilles pour grand model")
    casierperdu = models.IntegerField(null=True, default=0)
    produitperdu = models.IntegerField(null=True, default=0)
    casiercasse = models.IntegerField(null=True, default=0)
    produitcasse = models.IntegerField(null=True, default=0)

    etat_du_produit = (
        (u"Stock en cours", u"Stock en cours"),
        (u"Perte", u"Perte"),
        (u"Cassé", u"Cassé"),
        (u"Perte - Cassé", u"Perte - Cassé")
    )
    etat = models.BooleanField(null=True, default=False)

    # variables systemes
    total = models.IntegerField(null=True, blank=True)
    datecreationdepotstockproduit = models.DateField(auto_now_add=True, null=True)
    requete_achat = models.DateTimeField(null=True, blank=True)
    datemodificationdepotstockproduit = models.DateTimeField(auto_now_add=True, null=True)
    etatdepotstockproduit = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.parametreprixachatstockproduit)

    class Meta:
        ordering = ('-id',)


class RemboursementPoduit(models.Model):
    produit = models.ForeignKey(DepotStockProduit, on_delete=models.SET_NULL, null=True)
    payer = models.DecimalField(null=True, decimal_places=2, max_digits=15)
    totalpayer = models.DecimalField(null=True, decimal_places=2, max_digits=15)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('id',)


class HistoriquesDesAchats(models.Model):
    no_facture = models.CharField(max_length=15, null=True)
    date_achat = models.DateField(null=True)


class PanierStockProduit(models.Model):
    no_facture = models.CharField(max_length=15, null=True, blank=True, verbose_name='Numéro de facture')
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True)
    parametreprixachatstockproduit = models.ForeignKey(ParametrePrixAchatStockProduit,
                                                       on_delete=models.SET_NULL,
                                                       null=True,
                                                       verbose_name='Produit prix')
    quantitedepotstockproduit = models.IntegerField(null=True, blank=False, verbose_name="Quantité dépot stock produit")
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)

    # parametres systemes
    montantdepotstockproduit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nombrecasierequivalentdepotstockproduit = models.IntegerField(null=True, blank=True,
                                                                  help_text="24 bouteilles pour petit model et 12 "
                                                                            "bouteilles pour grand model")
    quantiterestantdepotstockproduit = models.IntegerField(null=True, blank=True)
    montantrestantdepotstockproduit = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                                          blank=True)
    nombrecasierequivalentrestantdepotstockproduit = models.IntegerField(null=True, blank=True,
                                                                         help_text="24 bouteilles pour petit model et "
                                                                                   "12 bouteilles pour grand model")
    casierperdu = models.IntegerField(null=True, default=0, verbose_name="Casier perdu")
    produitperdu = models.IntegerField(null=True, default=0, verbose_name="Produit perdu")
    casiercasse = models.IntegerField(null=True, default=0, verbose_name="Casier cassé")
    produitcasse = models.IntegerField(null=True, default=0, verbose_name="Produit cassé")

    # variables systemes
    panierdepot = models.BooleanField(default=True, null=True)
    datecreationdepotstockproduit = models.DateField(auto_now_add=True, null=True)
    datemodificationdepotstockproduit = models.DateTimeField(auto_now_add=True, null=True)
    etatdepotstockproduit = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.parametreprixachatstockproduit)

    class Meta:
        ordering = ('-id',)


class TotalDepotStockProduit(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True)
    parametreprixachatstockproduit = models.ForeignKey(ParametrePrixAchatStockProduit,
                                                       on_delete=models.SET_NULL,
                                                       null=True,
                                                       verbose_name='Produit prix')
    quantitedepotstockproduit = models.IntegerField(null=True, blank=False)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)

    # parametres systemes
    montantdepotstockproduit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nombrecasierequivalentdepotstockproduit = models.IntegerField(null=True, blank=True,
                                                                  help_text="24 bouteilles pour petit model et 12 "
                                                                            "bouteilles pour grand model")
    quantiterestantdepotstockproduit = models.IntegerField(null=True, blank=True)
    montantrestantdepotstockproduit = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                                          blank=True)
    nombrecasierequivalentrestantdepotstockproduit = models.IntegerField(null=True, blank=True,
                                                                         help_text="24 bouteilles pour petit model et "
                                                                                   "12 bouteilles pour grand model")
    casierperdu = models.IntegerField(null=True, default=0)
    produitperdu = models.IntegerField(null=True, default=0)
    casiercasse = models.IntegerField(null=True, default=0)
    produitcasse = models.IntegerField(null=True, default=0)

    etat = models.BooleanField(null=True, default=False)

    # variables systemes
    total = models.IntegerField(null=True, blank=True)
    datecreationdepotstockproduit = models.DateField(auto_now_add=True, null=True)
    requete_achat = models.DateTimeField(null=True, blank=True)
    datemodificationdepotstockproduit = models.DateTimeField(auto_now_add=True, null=True)
    etatdepotstockproduit = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.parametreprixachatstockproduit)

    class Meta:
        ordering = ('-id',)


"""
MODEL DES VENTE DE PRODUIT
"""


class ParamPrixProduitVente(models.Model):
    DETAILSPRIXPRODUIT = (
        (u'Casier entier', u'Casier entier'),
        (u'Trois-quart de casier', u'Trois-quart de casier'),
        (u'Démi-casier', u'Démi-asier '),
        (u'Quart de casier', u'Quart de casier'),
    )
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    detailprixvente = models.CharField(choices=DETAILSPRIXPRODUIT, max_length=25, null=True)
    prixreelle = models.DecimalField(max_digits=15, decimal_places=2, null=True, verbose_name="Prix réelle")
    prixarrondi = models.DecimalField(max_digits=15, decimal_places=2, null=True, verbose_name="Prix arrondi")
    remise = models.IntegerField(null=True, blank=True)

    datecreation = models.DateField(auto_now_add=True, null=True)
    datemodification = models.DateField(auto_now_add=True, null=True)
    etat = models.BooleanField(default=False, null=True)

    def __str__(self):
        if self.produit:
            return str(self.produit)


class Client(models.Model):
    libelleclient = models.CharField(max_length=100, null=True)
    adresse = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=100, null=True)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)
    datecreation = models.DateField(auto_now_add=True, null=True)
    datemodification = models.DateField(auto_now_add=True, null=True)
    etat = models.BooleanField(default=False, null=True)

    def __str__(self): return self.libelleclient


class VenteProduit(models.Model):
    no_facture = models.CharField(max_length=50, null=True, blank=True, verbose_name='Libelle de facture')
    paramprixproduitvente = models.ForeignKey(ParamPrixProduitVente, on_delete=models.SET_NULL, null=True)
    quantitevendu = models.IntegerField(null=True, verbose_name='Quantité vendu')
    casier = models.IntegerField(null=True, default=0, blank=True)
    montantvendu = models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Montant vendu', blank=True)
    montantarrondi = models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Montant arrondi', blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Client régulier')
    acheteur = models.CharField(max_length=100, null=True, blank=True, verbose_name='Client particulier')
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True, blank=True)

    bb_12 = models.IntegerField(null=True, default=0, verbose_name='Emballage bb de 12 consigné')
    bb_24 = models.IntegerField(null=True, default=0, verbose_name='Emballage bb de 24 consigné')
    snb_12 = models.IntegerField(null=True, default=0, verbose_name='Emballage snb de 12 consigné')
    snb_24 = models.IntegerField(null=True, default=0, verbose_name='Emballage snb de 24 consigné')

    # variable systeme
    produit = models.ForeignKey(DepotStockProduit, on_delete=models.SET_NULL, null=True)
    emballage = models.ForeignKey(TotalEmballage, on_delete=models.SET_NULL, null=True)

    # variable de base
    datecreation = models.DateField(auto_now_add=True, null=True)
    datemodification = models.DateField(auto_now_add=True, null=True)
    etat = models.BooleanField(default=False, null=True)

    def __str__(self): return self.paramprixproduitvente


class PanierVente(models.Model):
    no_facture = models.CharField(max_length=50, null=True, blank=True, verbose_name='Libelle de facture')
    paramprixproduitvente = models.ForeignKey(ParamPrixProduitVente, on_delete=models.SET_NULL, null=True)
    quantitevendu = models.IntegerField(null=True, verbose_name='Quantité vendu')
    casier = models.IntegerField(null=True, default=0, blank=True)
    montantvendu = models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Montant vendu', blank=True)
    montantarrondi = models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Montant arrondi', blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Client régulier')
    acheteur = models.CharField(max_length=100, null=True, blank=True, verbose_name='Client particulier')
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True, blank=True)

    bb_12 = models.IntegerField(null=True, default=0, verbose_name='Emballage bb de 12 consigné')
    bb_24 = models.IntegerField(null=True, default=0, verbose_name='Emballage bb de 24 consigné')
    snb_12 = models.IntegerField(null=True, default=0, verbose_name='Emballage snb de 12 consigné')
    snb_24 = models.IntegerField(null=True, default=0, verbose_name='Emballage snb de 24 consigné')

    # variable systeme
    produit = models.ForeignKey(DepotStockProduit, on_delete=models.SET_NULL, null=True)
    emballage = models.ForeignKey(TotalEmballage, on_delete=models.SET_NULL, null=True)

    # variable de base
    paniervente = models.BooleanField(default=True, null=True)
    datecreation = models.DateField(auto_now_add=True, null=True)
    datemodification = models.DateField(auto_now_add=True, null=True)
    etat = models.BooleanField(default=False, null=True)

    def __str__(self): return str(self.paramprixproduitvente)


class RetournerEmballage(models.Model):
    bb_12 = models.IntegerField(null=True, default=0, verbose_name='Caiser bb de 12 prêté au client')
    bb_24 = models.IntegerField(null=True, default=0, verbose_name='Caiser bb de 24 prêté au client')
    snb_12 = models.IntegerField(null=True, default=0, verbose_name='Caiser snb de 12 prêté au client')
    snb_24 = models.IntegerField(null=True, default=0, verbose_name='Caiser snb de 24 prêté au client')
    venteproduit = models.ForeignKey(VenteProduit, on_delete=models.SET_NULL, null=True)

    # variable de base
    datecreation = models.DateField(auto_now_add=True, null=True)
    datemodification = models.DateField(auto_now_add=True, null=True)
    etat = models.BooleanField(default=False, null=True)
