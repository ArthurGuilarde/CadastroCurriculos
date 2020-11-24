from django.db import models

# Create your models here.
class Vaga(models.Model):
  name = models.CharField(("Nome"), max_length=50)
  description = models.TextField(("Descrição"), blank=True)
  
  created_at = models.DateTimeField(("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(("Atualizado em"), auto_now=True)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Vaga'
    verbose_name_plural = 'Vagas'
    ordering=['name']