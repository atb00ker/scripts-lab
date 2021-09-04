from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


def send(request):
    subject = 'Hello, I am a Testmail'
    timeNow = datetime.now()
    message = 'This testmail was send on %s' % timeNow
    recipient_list = settings.EMAIL_RECEIPIENT
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Yippe, Now check Index for a Mail @ %s" % timeNow)
