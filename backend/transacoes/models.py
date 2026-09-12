from django.db import models

class Transacao(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    
    # Chaves Estrangeiras conectando aos seus outros apps
    categoria = models.ForeignKey('categorias.Categoria', on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"