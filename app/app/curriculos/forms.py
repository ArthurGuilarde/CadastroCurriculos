from django import forms
from django.db import models
from .models import Curriculo

class CurriculoCreateForm(forms.ModelForm):
  """
  A form that creates a user, with no privileges, from the given username and
  password.
  """
    
  def save(self, user):
    
    instance = super().save(commit=False)
    instance.user = user
    
    instance.save()

    return instance

  class Meta:
    model = Curriculo
    fields = ("url",)
  
