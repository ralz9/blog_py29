from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response('Вы успешно зарегистрировались. Вам отправлено письмо на почту с активацией ', status=201)



class ActivationAPIView(APIView):
    def get(self, request, activation_code):
        # try:
        #     user = User.objects.get(activation_code=activation_code)
        # except User.DoesNotExist:
        #     return Response('Нет такого кода', status=400)
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fileds=['is_activ', 'activation_code'])
        return Response('Успешно', status=200)


class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogautAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ... #Token удалить
        return Response('Это секретная информация')


class ChangePasswordAPIView(APIView):
    ...
    # смена пароля
# TODO реализовать ForgotPassword