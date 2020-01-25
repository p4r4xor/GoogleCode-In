from django.contrib import admin
from happinesspackets.messaging.models import Message, BlacklistedEmail

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'status', 'admin_approved_public', 'sender_approved_public', 'recipient_approved_public')
    list_filter = ('status','admin_approved_public', 'sender_approved_public', 'recipient_approved_public')

    fieldsets = (
        ('Sender Details', {
            'fields': ('sender_name', 'sender_email', 'sender_email_stripped', 'sender_email_token', 'sender_ip')
        }),
        ('Recipient Details', {
            'fields': ('recipient_name', 'recipient_email', 'recipient_email_stripped', 'recipient_email_token')
        }),
        ('Message Details', {
            'fields': ('identifier', 'status', 'message')
        }),
        ('Message Permissions', {
            'fields': (('sender_named', 'sender_approved_public', 'sender_approved_public_named'), ('recipient_approved_public', 'recipient_approved_public_named'), 'admin_approved_public')
        })
    )

@admin.register(BlacklistedEmail)
class MessageAdmin(admin.ModelAdmin):
    pass

