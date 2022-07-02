from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .models import Service

from django.conf import settings
# Create your views here.
def home(request):
    services = Service.objects.all()
    context = {
        'services': services,

    }
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        # message_email = request.POST.get('message-email')
        # message = request.POST.get('message')
        
        send_mail(
        subject = 'welcome',
        message = 'whats up',
        from_email = 'odamejoshua37@gmail.com',
        recipient_list = ['joshod27@gmail.com',],
        fail_silently = False,
        )


        context.update({'message_name':message_name})

        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context)
