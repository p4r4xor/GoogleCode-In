# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import factory
import pytest

class MessageModelFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'messaging.Message'

    sender_name = 'Sender sender'
    sender_email = 'sendersender@null'
    recipient_name = 'Recipient recipient'
    recipient_email = 'recipientrecipient+foo@null'
    sender_ip = '127.0.0.1'
    message = 'message content'


class BlacklistedEmailFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'messaging.BlacklistedEmail'

    email = 'emailemail@null'
    confirmation_ip = '127.0.0.1'

@pytest.mark.django_db
class TestMessageModel:
    
    def test_unique_identifier(self):
        obj1 = MessageModelFactory()
        obj2 = MessageModelFactory()
        assert obj1.identifier != obj2.identifier

