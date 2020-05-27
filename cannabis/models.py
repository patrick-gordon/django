from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.
class Strain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    subType = models.CharField(max_length=20)
    description = models.TextField(blank=True, max_length=250)


class Comments(Strain):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False)