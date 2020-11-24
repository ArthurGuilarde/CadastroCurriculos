from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Curriculo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  url = models.FileField(("Curriculo"), upload_to='curriculos', max_length=100, blank=True)
  
  created_at = models.DateTimeField(("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(("Atualizado em"), auto_now=True)


  def __str__(self):
      return str(self.user) + str(self.url)

  class Meta:
    verbose_name = 'Curriculo'
    verbose_name_plural = 'Curriculos'
    ordering=['user']