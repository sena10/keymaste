from django.contrib import admin
from .models import Aluguel,Funcionario,Sala,Chave

# Register your models here.
admin.site.register(Aluguel)
admin.site.register(Funcionario)
admin.site.register(Sala)
admin.site.register(Chave)
