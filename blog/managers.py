from django.db.models import Manager
import datetime


class PostManager(Manager):
    """Returns published posts that are not in the future."""
    def __init__(self, *args, **kwargs):
        self.filter_dict = dict(status__gte=2, publish__lte=datetime.datetime.now())
        super(PostManager, self).__init__(*args, **kwargs)
    
    def published(self):
        return self.get_query_set().filter(**self.filter_dict)

    def draft(self):
        return self.get_query_set().filter(status=1)
