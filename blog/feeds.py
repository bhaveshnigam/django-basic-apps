from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed
from django.core.urlresolvers import reverse
from basic.blog.models import Post


class BlogPostFeed(Feed):
    _site = Site.objects.get_current()
    title = '%s feed' % _site.name
    description = '%s posts feed.' % _site.name

    def link(self):
        return reverse('blog_index')

    def items(self):
        return Post.objects.published()[:10]

    def item_pubdate(self, item):
        return item.publish