from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def home(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # ! send email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['riyam.techcampus@gmail.com'],  # to email
        )
        return render(request, 'home.html', {'message_name': message_name})
    else:
        return render(request, 'home.html', {})
