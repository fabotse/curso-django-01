from django.contrib import admin
from .models import *

# Register your models here.

class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone' , 'email')


class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'assunto', 'colaborador')

admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Categoria)
admin.site.register(Chamado, ChamadoAdmin)