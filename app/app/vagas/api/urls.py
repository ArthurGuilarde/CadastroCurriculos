from django.urls import path
from .views import list_all_vagas, add_new_vaga

urlpatterns = [
    path('list', list_all_vagas, name='list'),
    path('add', add_new_vaga, name='add'),
    
]
