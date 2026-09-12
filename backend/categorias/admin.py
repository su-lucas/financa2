from django.contrib import admin

from backend.categorias.models import Categoria

# Register your models here.
#colocando o administrador para poder ver os modelos no admin do django
admin.site.register(Categoria)