from django.contrib import admin

# Register your models here.
from .models import CoronicStatusOfRegion, CoronicStatusOfKorea

admin.site.register(CoronicStatusOfRegion)
admin.site.register(CoronicStatusOfKorea)