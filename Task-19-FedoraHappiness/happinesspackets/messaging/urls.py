from __future__ import unicode_literals

from django.urls import re_path

from .views import (StartView, MessageSearchView, MessageSendView, MessageSenderConfirmationSentView, MessageSenderConfirmationView,
                    MessageSenderConfirmedView, MessageRecipientMessageUpdate, MessageSenderPermissionsUpdate,FaqView, ArchiveView, InspirationView,
                    BlacklistEmailView, ReceivedMessagesView, SentMessagesView, FasidSearchView)

app_name = 'messaging'

urlpatterns = [
    re_path(r'^$', StartView.as_view(), name='start'),
    re_path(r'^faq/$', FaqView.as_view(), name='faq'),
    re_path(r'^archive/$', ArchiveView.as_view(), name='archive'),
    re_path(r'^inspiration/$', InspirationView.as_view(), name='inspiration'),
    re_path(r'^received-messages/$', ReceivedMessagesView.as_view(), name='received_messages'),
    re_path(r'^sent-messages/$', SentMessagesView.as_view(), name='sent_messages'),
    re_path(r'^blacklist-email/(?P<email>[\w\.@\+-]+)/(?P<digest>\w+)/$', BlacklistEmailView.as_view(), name='blacklist_email'),
    re_path(r'^send/$', MessageSendView.as_view(), name='send'),
    re_path(r'^send/confirmation-sent/$', MessageSenderConfirmationSentView.as_view(), name='sender_confirmation_sent'),
    re_path(r'^send/confirmation/(?P<identifier>[\w-]+)/(?P<token>[\w-]+)/$', MessageSenderConfirmationView.as_view(), name='sender_confirm'),
    re_path(r'^send/confirmed/$', MessageSenderConfirmedView.as_view(), name='sender_confirmed'),
    re_path(r'^recipient/(?P<identifier>[\w-]+)/(?P<token>[\w-]+)/$', MessageRecipientMessageUpdate.as_view(), name='recipient_message_update'),
    re_path(r'^sender/(?P<identifier>[\w-]+)/(?P<token>[\w-]+)/$', MessageSenderPermissionsUpdate.as_view(), name='sender_message_update'),
    re_path(r'^send/search/$', FasidSearchView.fasidCheck, name='fasid_check'),
    re_path(r'^search/?$', MessageSearchView.as_view(), name='search'),
]
