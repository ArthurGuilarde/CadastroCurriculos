from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.renderers import JSONRenderer

from django.contrib.auth.models import User
from .serializers import UserSerializer

@api_view(['GET'], )
@authentication_classes([])
@permission_classes([])
def list_all_users(request):
  if request.method == 'GET':
    try:
      users = User.objects.all()
      serializer = UserSerializer(users, many=True)
      
      return Response(serializer.data)
      
    except ValueError:
      return Response(status=status.HTTP_404_NOT_FOUND)



