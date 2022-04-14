from django.contrib.auth.models import User
from django.db import models

from agency.models import Agency

class Client(models.Model):

    # TIPOLOGIA CLIENTE
    CLIENTE = 'cliente'
    INVESTITORE = 'investitore'
    PROPRIETARIO = 'proprietario'

    CLIENT_TYPE = (
        (CLIENTE,'In asta'),
        (INVESTITORE, 'Investitore'),
        (PROPRIETARIO, 'Proprietario'),
    )

    # TITOLO CLIENTE
    SIGNORE = 'signore'
    SIGNORA = 'signora'
    DOTTORE = 'dottore'
    DOTTORESSA = 'dottoressa'
    GEOMETRA = 'geometra'

    CLIENT_TITLE = (
    (SIGNORE, 'Sig.'),
    (SIGNORA, 'Sig.ra'),
    (DOTTORE, 'Dott.'),
    (DOTTORESSA, 'Dott.ssa'),
    (GEOMETRA, 'Geom.'),
    )

    # STATUS ANNUNCIO
    ATTIVO = 'active'
    SOSPESO = 'suspended'
    SCADUTO = 'expired'

    STATUS = (
        (ATTIVO,'Attivo'),
        (SOSPESO, 'Sospeso'),
        (SCADUTO, 'Scaduto'),
    )

    agent = models.ForeignKey(Agency, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True)    
    surname = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255,choices=CLIENT_TYPE,default=CLIENTE)
    title = models.CharField(max_length=255, choices=CLIENT_TITLE,default='')
    contact_person = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    phone1 = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255, blank=True, null=True)
    phone3 = models.CharField(max_length=255,blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS, default=ATTIVO)
    address = models.CharField(max_length=255, blank=True, null=True)
    civico = models.CharField(max_length=25, blank=True, null=True)
    zona = models.CharField(max_length=255, blank=True, null=True)
    comune = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)
    regione = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=7, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Note(models.Model):
    agent = models.ForeignKey(Agency, related_name='notes', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='notes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)