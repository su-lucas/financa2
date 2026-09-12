from django.contrib import admin

from .models import Categoria

# Register your models here.
#colocando o administrador para poder ver os modelos no admin do django
admin.site.register(Categoria)