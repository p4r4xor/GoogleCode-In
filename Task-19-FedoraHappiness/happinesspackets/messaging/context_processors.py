from .models import Message

def packets_sent_processor(request):
    packets_sent = Message.objects.exclude(status="pending_sender_confirmation").count()
    return {'packets_sent': packets_sent}
