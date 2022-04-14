from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Agency
from .serializers import AgencySerializer, UserSerializer

class AgencyViewSet(viewsets.ModelViewSet):
    serializer_class = AgencySerializer
    queryset = Agency.objects.all()

    def get_queryset(self):
        return self.queryset.filter(agents__in=[self.request.user]).first()
    
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.agents.add(self.request.user)
        obj.save()


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_my_agency(request):
    agency = Agency.objects.filter(agents__in=[request.user]).first()
    serializer = AgencySerializer(agency)

    return Response(serializer.data)

@api_view(['POST'])
def add_agent(request):
    agency = Agency.objects.filter(agents__in=[request.user]).first()
    email = request.data['email']

    print('Email', email)

    user = User.objects.get(username=email)

    agency.agents.add(user)
    agency.save()

    return Response()