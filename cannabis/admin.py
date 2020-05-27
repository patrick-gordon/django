from django.contrib import admin
from .models import Strain
from .models import Comments

# Register your models here.
admin.site.register(Strain)
admin.site.register(Comments)
