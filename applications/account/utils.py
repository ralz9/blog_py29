from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Py29',
        f'Привет перейди по этой ссылке что бы активировать аккаунт: \n\nhttp://localhost:8000/api/account/activate/{code}',
        'ralz9-ralz9@mail.ru',
        [email]
    )

