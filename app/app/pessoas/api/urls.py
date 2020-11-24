from django.urls import path
from .views import list_all_users

urlpatterns = [
    path('list', list_all_users, name='list'),   
]
