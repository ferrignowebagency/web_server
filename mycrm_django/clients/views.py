from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import viewsets

from agency.models import Agency

from .models import Client, Note
from .serializers import ClientSerializer

from .serializers import ClientSerializer, NoteSerializer

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    
    def perform_create(self, serializer):
        agent = Agency.objects.filter(agents__in=[self.request.user]).first()

        serializer.save(agent=agent, created_by=self.request.user)

    def get_queryset(self):
        agent = Agency.objects.filter(agents__in=[self.request.user]).first()

        return self.queryset.filter(agent=agent)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        agent = Agency.objects.filter(agents__in=[self.request.user]).first()
        client_id = self.request.GET.get('client_id')

        return self.queryset.filter(agent=agent).filter(client_id=client_id)

    def perform_create(self, serializer):
        agent = Agency.objects.filter(agents__in=[self.request.user]).first()
        client_id = self.request.data['client_id']

        serializer.save(agent=agent, created_by=self.request.user, client_id=client_id)