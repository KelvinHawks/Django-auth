from rest_framework.decorators import api_view #excecute views involved with rest api
from rest_framework.response import Response #json response


@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def signup(requests):
    return Response({})

@api_view(['POST'])
def test_token(requests):
    return Response({})