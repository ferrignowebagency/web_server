from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import viewsets

from agency.models import Agency

from .models import Annunci
from .serializers import AnnunciSerializer

class AnnunciViewSet(viewsets.ModelViewSet):
    serializer_class = AnnunciSerializer
    queryset = Annunci.objects.all()
    
    def perform_create(self, serializer):
        agency = Agency.objects.filter(agents__in=[self.request.user]).first()

        serializer.save(agency=agency, created_by=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()

        agent_id = self.request.data['assigned_to']

        if agent_id:
            user = User.objects.get(pk=agent_id)
            serializer.save(assigned_to=user)
        else:
             serializer.save()

    def get_queryset(self):
        agency = Agency.objects.filter(agents__in=[self.request.user]).first()

        return self.queryset.filter(agency=agency)
