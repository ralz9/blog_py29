from django.urls import path

from applications.account.views import RegisterAPIView, ActivationAPIView, LoginAPIView, LogautAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>', ActivationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogautAPIView.as_view())

    # path('login/', ...),
]
