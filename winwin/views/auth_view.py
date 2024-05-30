from contextvars import Token
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from winwin.models.user import User
from winwin.serializers.user_serializers import UserSerializer

from rest_framework import status  # Import the missing module

class UserRegistrationView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Fix the status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        # Récupérer les données d'identification de la requête
        email = request.data.get('email')
        password = request.data.get('password')

        # Recherche de l'utilisateur dans la base de données
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # L'utilisateur n'existe pas
            return Response({'error': 'Invalid email'}, status=401)

        # Vérification du mot de passe
        if not user.check_password(password):
            # Le mot de passe est incorrect
            return Response({'error': 'Invalid password'}, status=401)

        # L'utilisateur est authentifiés
        token = 'tken beer'
        user_data = {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'is_user_sponsor': user.is_user_sponsor,
                        'is_streamer': user.is_streamer,
                        'phone_number': user.phone_number,
                        'bio': user.bio,
                    }
        return Response({'success': 'User authenticated',
                                 'user': user_data,
                                 'token': token})