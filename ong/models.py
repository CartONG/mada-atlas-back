#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.gis.db import models as gismodels
from django.contrib.auth.models import User
from django.utils.timezone import now

"""
# Create your models here.
# Les "Primary Key" de chaque classe sont générées automatiquement 
"""

class organisme(models.Model):
    nom = models.CharField(max_length=40)
    description = models.TextField(null=True)
    logo = models.ImageField(upload_to="static/media/logo/%Y/%m", blank=True, null=True)
    status = models.ForeignKey('status', verbose_name="status") # Un "status" peut qualifier plrs "organisme" et un "organisme" ne peut avoir qu'un statut"  => Pas OneToOneField ni "OneToManyField" qui n'existe pas en Django mais ForeignKey## la class status n'est pas encore défini, j'utilise donc le nom du modeleÃ  la place de l'objet model lui-mÃme
    referent = models.ForeignKey('self', blank=True, null=True)

    # Ainsi le model est correctement definit dans admin.
    class Meta:
        verbose_name = 'organisme'
        verbose_name_plural = "organismes"
        ordering = ['nom']

    # Retourne la chaîne de caractère définissant le modèle.
    def __unicode__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que nous
        traiterons plus tard et dans l'administration
        """
        return u"Organisme: %s" % self.nom

    # Retourne un court descriptif
    def short(self):
        return u"%s - %s" % (self.status, self.nom)
    short.allow_tags = True


class status(models.Model):
    STATUS = (
        (u'ong', u'ONG'),
        (u'bailleur', u'Bailleur'),
        (u'organisation', u'Organisation'),
    )
    nom = models.CharField(max_length=40, choices=STATUS)
    
    class Meta:
        verbose_name_plural = "status"
    
    def __unicode__(self):
        return u"Status: %s" % self.nom

   
class utilisateur(models.Model):
    user = models.OneToOneField(User) # La liaison OneToOne vers le modèle User (mail-nom-prenom-password)
    photo = models.ImageField(upload_to="static/media/photos/%Y/%m", blank=True, null=True)
    organisme = models.ForeignKey(organisme) # Va servir plus tard de groupe pour inclure les "users"
    is_responsable = models.BooleanField("Responsable autorisé à éditer la fiche", default=False)

    class Meta:
        verbose_name = "utilisateur"
        verbose_name_plural = "utilisateurs"
        ordering = ['user']

    def __unicode__(self):
        return u"User: %s" % self.user.username

    def appartenance(self):
        "Returns the organisme and person's full name."
        return u"%s %s : %s" % (self.first_name, self.last_name, self.organisme)
    appartenance.allow_tags = True
    affiliation = property(appartenance)

class action(models.Model):
    titre = models.CharField(max_length = 100)
    date = models.DateTimeField("Date de démarrage", auto_now_add=False, auto_now=False)
    duree = models.CharField(max_length=40)
    description = models.TextField(null=True)
    localisation = models.CharField(max_length=50)
    illustration = models.ImageField(upload_to="static/media/illustration/%Y/%m", blank=True, null=True)
    responsable = models.ForeignKey(utilisateur, limit_choices_to={'is_responsable': True}, verbose_name="nom du responsable de la fiche")
    organisme = models.ForeignKey(organisme, verbose_name="organisme maitre d'oeuvre")
    avancement = models.ForeignKey('avancement', verbose_name="état d'avancement") # Un "avancement" peut concerner plrs "actions" mais une "action" ne peut avoir qu'un état d'"avancement" => ForeignKey
    categories = models.ManyToManyField('categorie', verbose_name="catégorie") # Un ou plrs "catégories" peut qualifier une "action" et une "action" peut agir dans un ou plrs "catégories"  => ManyToManyField
    creation = models.DateTimeField("Date de création fiche", auto_now_add=True)
    maj = models.DateTimeField("Date de mise à jour fiche", auto_now_add=True)
    geom = gismodels.PointField(srid=3857,default='SRID=3857;POINT(0.0 0.0)')

    objects = gismodels.GeoManager()
     
    class Meta:
        verbose_name = "action"
        verbose_name_plural = "actions"
        ordering = ['-creation']
        
    def __unicode__(self):
        return u"Action: %s" % self.titre

    # Retourne un rapide descriptif
    def short(self):
        return u"%s - %s\n%s - %s" % (self.titre, self.date.strftime("%b %d, %I:%M %p"), self.avancement)
    short.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.creation = now()
        self.maj = now()
        super(action, self).save(*args, **kwargs)


    # Controle de l'ancienneté de la fiche
    #def control_obsolescence(self):
    #    "Returns action's obsolescence record status."
    #Vérifier si le status actuel d'avancement n'est pas "Terminé" et que la date de "maj" est supérieur à 1 an..


class avancement(models.Model):
    AVANCEMENT = (
        (u'en attente', u'En attente'),
        (u'en_cours', u'En cours'),
        (u'Terminé', u'Terminé'),
    )

    nom = models.CharField(max_length=40, choices=AVANCEMENT)

    class Meta:
        verbose_name_plural = "Avancements"

    def __unicode__(self):
        return u"Avancement: %s" % self.nom

class categorie(models.Model):
    CATEGORIE = (
        (u'environnement', u'Environnement'),
        (u'tourisme', u'Tourisme'),
        (u'développement rural', u'Développement rural'),
        (u'eau/assainissement', u'Eau/Assainissement'),
        (u'santé', u'Santé'),
        (u'éducation', u'Éducation'),
        (u'justice', u'Justice'),
	(u'formation conseil', u'Formation Conseil'),
	(u'protection sociale', u'Protection Sociale'),
	(u'micro-crédit', u'Micro-Crédit'),
    )

    nom = models.CharField(max_length=40, choices=CATEGORIE)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u"Catégorie: %s" % self.nom

