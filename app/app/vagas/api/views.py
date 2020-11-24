from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.renderers import JSONRenderer

from app.vagas.models import Vaga
from .serializers import VagaSerializer

@api_view(['GET'], )
@authentication_classes([])
@permission_classes([])
def list_all_vagas(request):
  if request.method == 'GET':
    try:
      vagas = Vaga.objects.all()
      serializer = VagaSerializer(vagas, many=True)
      
      return Response(serializer.data)
      
    except ValueError:
      return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'], )
@authentication_classes([])
@permission_classes([])
def add_new_vaga(request):
  if request.method == 'POST':
    print(request.data)
    serializer = VagaSerializer(data = request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

  


