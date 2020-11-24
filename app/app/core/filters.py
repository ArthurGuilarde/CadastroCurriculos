import django_filters
from app.vagas.models import Vaga

class VagasFilter(django_filters.FilterSet):

  class Meta:
    model = Vaga
    fields = {
      'name':['icontains'],
      'description':['icontains']
    }