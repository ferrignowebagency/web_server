from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

from agency.models import Agency

class Annunci(models.Model):
    # TIPO ANNUNCIO
    ASTA = 'asta'
    MERCATO_LIBERO = 'mercato_libero'

    CHOICES_SELL_TYPE = (
        (ASTA,'In asta'),
        (MERCATO_LIBERO, 'Mercato libero'),
    )

    # STATUS ANNUNCIO
    ATTIVO = 'active'
    SOSPESO = 'suspended'
    SCADUTO = 'expired'
    BAD_QUALITY = 'bad_quality'
    LOW_QUALITY = 'low_quality'

    STATUS = (
        (ATTIVO,'Attivo'),
        (SOSPESO, 'Sospeso'),
        (SCADUTO, 'Scaduto'),
        (BAD_QUALITY, 'Scarsa qualità'),
        (LOW_QUALITY, 'Bassa qualità')
    )

    # ESITO ASTA
    LOST = 'lost'
    WON = 'won'

    CHOICES_RESULTS = (
        (LOST, 'Persa'),
        (WON, 'Vinta')
    )

    # TIPOLOGIA IMMOBILE
    APPARTAMENTO = 'appartamento'
    VILLA = 'villa'
    TERRENO = 'terreno'
    NEGOZIO = 'negozio'

    CHOICES_TYPOLOGY = (
        (APPARTAMENTO, 'Appartamento'),
        (VILLA, 'Villa'),
        (TERRENO, 'Terreno'),
        (NEGOZIO, 'Negozio')
    )

    agency = models.ForeignKey(Agency, related_name='annunci', on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True)
    sell_type = models.CharField(max_length=30, choices=CHOICES_SELL_TYPE, default=ASTA)
    type_immobile = models.CharField(max_length=30, choices=CHOICES_TYPOLOGY, blank=True, default='')
    company = models.CharField(max_length=255)
    descrizione = models.CharField(max_length=500, blank=True, null=True)
    contact_person = models.CharField(max_length=255)
    prezzo_uno = models.CharField(max_length=25,blank=True, null=True)
    prezzo_due = models.CharField(max_length=25,blank=True, null=True)
    prezzo_tre = models.CharField(max_length=25,blank=True, null=True)
    prezzo_quattro = models.CharField(max_length=25,blank=True, null=True)
    quality = models.CharField(max_length=3,blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    civico = models.CharField(max_length=25, blank=True, null=True)
    zona = models.CharField(max_length=255, blank=True, null=True)
    comune = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)
    regione = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=7, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS, default=ATTIVO)
    result = models.CharField(max_length=25, choices=CHOICES_RESULTS, blank=True, default='')
    assigned_to = models.ForeignKey(User, related_name='assigned_annuncio', blank=True, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='annunci', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)