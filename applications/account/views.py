from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response('Вы успешно зарегистрировались. Вам отправлено письмо на почту с активацией ', status=201)


