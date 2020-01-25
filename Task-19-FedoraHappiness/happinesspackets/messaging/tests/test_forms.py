from ..forms import check_recipient_is_sender
from django.test import TestCase


class TestIsReceipientEqualsSenderEmail(TestCase):

    def test_should_return_true_for_same_sender_and_recipient(self):
        sender_email = []
        recipient_email = []
        sender_email.append('user@gmail.com')
        recipient_email.append('user@gmail.com')
        self.assertTrue(check_recipient_is_sender(sender_email, recipient_email))

    def test_should_return_false_for_different_sender_and_recipient(self):
        sender_email = []
        recipient_email = []
        sender_email.append('user+sender@gmail.com')
        recipient_email.append('user2+fedora@gmail.com')
        self.assertFalse(check_recipient_is_sender(sender_email, recipient_email))