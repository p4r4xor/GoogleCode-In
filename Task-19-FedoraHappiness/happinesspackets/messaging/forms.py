# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from datetime import timedelta

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML
from django import forms
from django.conf import settings
from django.urls import reverse
from django.db.models import Q
from django.utils import timezone
import bleach

from .models import Message, strip_email

logger = logging.getLogger(__name__)

def check_recipient_is_sender(sender_emails, recipient_emails) -> bool:
    if not (set(sender_emails).isdisjoint(recipient_emails)):
        return True
    else:
        return False

def validate_email_is_rate_limited(email):
    timeframe = timezone.now() - timedelta(hours=24)
    stripped_email = strip_email(email)
    recent_message_count = Message.objects.filter(Q(sender_email_stripped=stripped_email) | Q(recipient_email_stripped=stripped_email), created__gte=timeframe).count()
    if recent_message_count > settings.MAX_MESSAGES:
        raise forms.ValidationError("We can't send emails to this address at this time. You can try again in 24 hours.")


class MessageSendForm(forms.ModelForm):
    # hp = forms.CharField(label="do not fill", required=False)
    fasid = forms.CharField(label="FAS Username", required=False)

    class Meta:
        model = Message
        fields = ['recipient_name', 'recipient_email', 'message',
                  'sender_named', 'sender_approved_public', 'sender_approved_public_named']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(MessageSendForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-8'

        self.fields['recipient_name'].label = 'Name'
        self.fields['recipient_email'].label = 'Email'
        self.fields['recipient_email'].validators = [validate_email_is_rate_limited]
        self.fields['message'].help_text = 'Writer\'s block? Check out our <a href="%s">message inspiration</a>.' % reverse('messaging:inspiration')
        self.fields['sender_named'].label = 'I agree to share my name and email address with the recipient.'
        self.fields['sender_approved_public'].label = "I agree to publish this message and display it publicly in the Happiness Archive."
        self.fields['sender_approved_public_named'].label = "... and I agree to display our names publicly too."
        self.fields['sender_approved_public_named'].help_text = "Note: We only publish information if both the sender and the recipients agree."

        self.helper.layout = Layout(
            # Fieldset('This Happiness Packet is from...', 'sender_name', 'sender_email', 'hp'),
            Fieldset("Search for a FAS Username", 'fasid' ),
            Fieldset("Send this Happiness Packet to...", 'recipient_name', 'recipient_email'),
            Fieldset("Your message is...", 'message'),
            Fieldset("Privacy and permissions", 'sender_named', 'sender_approved_public', 'sender_approved_public_named'),
            HTML("<br>"),
            Submit('submit', 'Send some happiness', css_class='btn-lg centered'),
        )
    
    def clean_message(self): 
        """ Cleans given HTML with bleach.clean() """

        allowed_tags = set(bleach.ALLOWED_TAGS + [ 
            'a', 'blockquote', 'code', 'del', 'dd', 'dl', 'dt', 
            'h1', 'h2', 'h3', 'h3', 'h4', 'h5', 'i', 'img', 'kbd', 
            'li', 'ol', 'ul', 'p', 'pre', 's', 'sup', 'sub', 'em', 
            'strong', 'strike', 'ul', 'br', 'hr', ]) 

        allowed_styles = set(bleach.ALLOWED_STYLES + [ 
            'color', 'background-color', 'font', 'font-weight', 
            'height', 'max-height', 'min-height', 
            'width', 'max-width', 'min-width', ]) 

        allowed_attributes = {}   
        allowed_attributes.update(bleach.ALLOWED_ATTRIBUTES) 
        allowed_attributes.update({ 
            '*': ['class', 'title'], 
            'a': ['href', 'rel'], 
            'img': ['alt', 'src', 'width', 'height', 'align', 'style', 'max-width'], 
        }) 
        html = self.cleaned_data['message']
        return bleach.clean(
            html, 
            strip=True,
            tags=allowed_tags, 
            attributes=allowed_attributes, 
            styles=allowed_styles
        ) 

    def clean(self):
        super(MessageSendForm, self).clean()
        sender_emails = []
        sender_emails.append(self.user.email)
        sender_emails.append(strip_email(self.user.email))
        sender_emails.append(self.user.username + '@fedoraproject.org')
        recipient_emails = []
        recipient_email = self.cleaned_data.get('recipient_email')
        recipient_emails.append(recipient_email)
        if recipient_email:                     #Before clean(), validation is performed, which removes recipient_email field if validation is failed
            recipient_emails.append(strip_email(recipient_emails[0]))

            if check_recipient_is_sender(sender_emails, recipient_emails):
                raise forms.ValidationError("You cannot send a Fedora Happiness Packet to yourself!")
            elif self.cleaned_data.get('sender_approved_public_named') and not self.cleaned_data.get('sender_approved_public'):
                self.add_error('sender_approved_public_named', "If you want us to publish the message including your names, "
                                                                "you must also check 'I agree to publish this message and"
                                                                "display it publicly in the Happiness Archive'")
        validate_email_is_rate_limited(self.user.email)

    

class MessageRecipientForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient_approved_public', 'recipient_approved_public_named']

    def __init__(self, *args, **kwargs):
        super(MessageRecipientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-8'

        self.fields['recipient_approved_public'].label = "I agree to publish this message and display it publicly in the Happiness Archive."
        self.fields['recipient_approved_public_named'].label = "... and I agree to display our names publicly too."
        self.fields['recipient_approved_public_named'].help_text = "Note: We only publish information if both the sender and the recipients agree."

        self.helper.layout = Layout(
            Fieldset("Privacy and permissions", 'recipient_approved_public', 'recipient_approved_public_named'),
            HTML("<br>"),
            Submit('submit', 'Save privacy choices', css_class='btn-lg centered'),
        )

    def clean(self):
        super(MessageRecipientForm, self).clean()
        if self.cleaned_data.get('recipient_approved_public_named') and not self.cleaned_data.get('recipient_approved_public'):
            self.add_error('recipient_approved_public_named', "If you want us to publish the message including your "
                                                              "names, you must also check 'I agree to publish this "
                                                              "message and display it publicly in the Happiness "
                                                              "Archive.'")
class MessageSenderPermissionForm(forms.ModelForm):
    class Meta: 
        model = Message 
        fields = ['sender_named', 'sender_approved_public', 'sender_approved_public_named']

    def __init__(self, *args, **kwargs):
        super(MessageSenderPermissionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-8'

        self.fields['sender_named'].label = 'I agree to share my name and email address with the recipient.'
        self.fields['sender_approved_public'].label = "I agree to publish this message and display it publicly in the Happiness Archive."
        self.fields['sender_approved_public_named'].label = "... and I agree to display our names publicly too."
        self.fields['sender_approved_public_named'].help_text = "Note: We only publish information if both the sender and the recipients agree."

        self.helper.layout = Layout(
            Fieldset("Privacy and permissions", 'sender_named', 'sender_approved_public', 'sender_approved_public_named'),
            HTML("<br>"),
            Submit('submit', 'Send some happiness', css_class='btn-lg centered'),
        )
    
    def clean(self):
        super(MessageSenderPermissionForm, self).clean()
        if self.cleaned_data.get('sender_approved_public_named') and not self.cleaned_data.get('sender_approved_public'):
            self.add_error('sender_approved_public_named', "If you want us to publish the message including your names, "
                                                           "you must also check 'I agree to publish this message and"
                                                           "display it publicly in the Happiness Archive'")
