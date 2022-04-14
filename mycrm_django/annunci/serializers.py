from rest_framework import serializers

from .models import Annunci
from agency.serializers import UserSerializer

class AnnunciSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    class Meta:
        model = Annunci
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'title',
            'sell_type',
            'type_immobile',
            'company',
            'contact_person',
            'descrizione',
            'prezzo_uno',
            'prezzo_due',
            'prezzo_tre',
            'prezzo_quattro',
            'quality',
            'address',
            'civico',
            'zona',
            'comune',
            'provincia',
            'regione',
            'zip_code',
            'latitude',
            'longitude',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'result',
            'assigned_to',
            'created_at',
            'modified_at',
        )