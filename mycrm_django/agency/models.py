from django.contrib.auth.models import User
from django.db import models

class Agency(models.Model):
    name = models.CharField(max_length=255)
    agents = models.ManyToManyField(User, related_name='agency')
    created_by = models.ForeignKey(User, related_name='created_agency', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)