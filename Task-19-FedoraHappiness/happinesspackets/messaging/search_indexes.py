from haystack import indexes
from .models import Message

class MessageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Message

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(sender_approved_public=True, recipient_approved_public=True, admin_approved_public=True)
