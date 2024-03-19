from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.tokens import RefreshToken



@swagger_auto_schema(
    method='post',
    request_body=UserSerializer,  # Указываем, что тело запроса должно быть сериализовано с помощью LoginSerializer
    responses={
        200: openapi.Response('Successful Login', UserSerializer),
        400: 'Invalid Credentials'
    }
)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(
    method='post',
    request_body=LoginSerializer,  # Указываем, что тело запроса должно быть сериализовано с помощью LoginSerializer
    responses={
        200: openapi.Response('Successful Login', LoginSerializer),
        400: 'Invalid Credentials'
    }
)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    refresh = RefreshToken.for_user(user)

    return Response({
        'user': user.username,
        'access_token': str(refresh.access_token),
        'refresh_token': str(refresh),
    })