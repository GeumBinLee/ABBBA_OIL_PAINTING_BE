from django.contrib import admin
from painters.models import Painting, Painter

admin.site.register(Painter)
admin.site.register(Painting)