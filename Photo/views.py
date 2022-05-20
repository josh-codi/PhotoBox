from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

from django.conf import settings
# Create your views here.
def home(request):
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')

        send_mail(
            message_name,
            f'From: {message_email}\n\n-----------\n\n{message}',
            message_email,
            ['odamejoshua37@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})
