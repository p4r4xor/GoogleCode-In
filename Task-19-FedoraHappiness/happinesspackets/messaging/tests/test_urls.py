from django.urls import reverse, resolve

class TestUrls:

    def test_start_url(self):
        path = reverse('messaging:start')
        assert resolve(path).view_name == 'messaging:start' 

    def test_faq_url(self):
        path = reverse('messaging:faq')
        assert resolve(path).view_name == 'messaging:faq'    
    
    def test_archive_url(self):
        path = reverse('messaging:archive')
        assert resolve(path).view_name == 'messaging:archive'

    def test_inspiration_url(self):
        path = reverse('messaging:inspiration')
        assert resolve(path).view_name == 'messaging:inspiration'

    def test_received_messages_url(self):
        path = reverse('messaging:received_messages')
        assert resolve(path).view_name == 'messaging:received_messages'

    def test_sent_messages_url(self):
        path = reverse('messaging:sent_messages')
        assert resolve(path).view_name == 'messaging:sent_messages' 

    def test_blacklist_email_url(self):
        path = reverse('messaging:blacklist_email', kwargs = {'email':'foobar@gmail.com','digest':'f47850e34f1588b79e5970d409325625264b7d60'})
        assert resolve(path).view_name == 'messaging:blacklist_email'

    def test_send_url(self):
        path = reverse('messaging:send')
        assert resolve(path).view_name == 'messaging:send'

    def test_sender_confirmation_sent_url(self):
        path = reverse('messaging:sender_confirmation_sent')
        assert resolve(path).view_name == 'messaging:sender_confirmation_sent'

    def test_sender_confirm_url(self):
        path = reverse('messaging:sender_confirm', kwargs = {'identifier':'M4ZK-R88T-BTGC-MTDM', 'token':'M4ZK-R88T-BTGC-MTDM'})
        assert resolve(path).view_name == 'messaging:sender_confirm'

    def test_sender_confirmed_url(self):
        path = reverse('messaging:sender_confirmed')
        assert resolve(path).view_name == 'messaging:sender_confirmed'
   
    def test_recipient_message_update_url(self):
        path = reverse('messaging:recipient_message_update', kwargs = {'identifier':'M4ZK-R88T-BTGC-MTDM', 'token':'M4ZK-R88T-BTGC-MTDM'})
        assert resolve(path).view_name == 'messaging:recipient_message_update'

    def test_fasid_check_url(self):
        path = reverse('messaging:fasid_check')
        assert resolve(path).view_name == 'messaging:fasid_check'

    def test_search_url(self):
        path = reverse('messaging:search')
        assert resolve(path).view_name == 'messaging:search'