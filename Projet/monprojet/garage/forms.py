from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class VoitureForm(ModelForm):
    class Meta:
        model = models.Voiture
        fields = ('marque', 'modele', 'annee', 'couleur', 'immatriculation')
        labels = {
            'marque' : _('Marque de la voiture'),
            'modele' : _('Modèle de la voiture'),
            'annee' : _('Année de la voiture'),
            'couleur' : _('Couleur de la voiture'),
            'immatriculation' : _('Immatriculation de la voiture'),
        }