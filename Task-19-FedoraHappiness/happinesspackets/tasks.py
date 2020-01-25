import logging

from email.mime.image import MIMEImage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def send_html_mail(subject, body_txt, body_html, recipient):
    message = EmailMultiAlternatives(subject, body_txt, settings.DEFAULT_FROM_EMAIL, [recipient])
    message.attach_alternative(body_html, 'text/html')
    message.mixed_subtype = 'related'

    logo_file = open(settings.STATIC_ROOT.child('images').child('logo.png'), 'rb')
    logo_mime = MIMEImage(logo_file.read())
    logo_file.close()
    logo_mime.add_header('Content-ID', '<logo.png@happinesspackets.io>')
    logo_mime.add_header('Content-Disposition', 'attachment')

    message.attach(logo_mime)
    message.send()
