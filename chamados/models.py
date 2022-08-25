from django.db import models

# Create your models here.
class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200 ,null=True)
    telefone = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Chamado(models.Model):
    STATUS = (
        ('Aberto', 'Aberto'),
        ('Em atendimento', 'Em atendimento'),
        ('Finalizado', 'Finalizado')
    )

    colaborador = models.ForeignKey(Colaborador, null=True, on_delete=models.SET_NULL)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)
    assunto = models.CharField(null=True, blank=False, max_length=200)
    descricao = models.TextField(blank=False, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)

    def __str__(self):
        return self.assunto