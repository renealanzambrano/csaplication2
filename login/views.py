from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# NECESITAMOS UN TIPO DE RESPUESTA JSON
from rest_framework.response import Response
# funciones basadas en clase 
class CustomAuthToken(ObtainAuthToken):
    # self es un aputador, apunta al metodo de una misma clase
    # request establece la comunicacion y la envia
    # args
    def post(self, request,*args,**kwarsg):
        serializer = self.serializer_class(data=request.data, context= {'request':request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user) #variables con mismo valor

        return Response({
            'token':token.key,
            'user_id': user.pk,
            'email':user.email,
            'username':user.username,
        }
        )