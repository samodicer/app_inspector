from django.contrib import admin

from . models import Document
from . models import Analyse

admin.site.register(Document)
admin.site.register(Analyse)
