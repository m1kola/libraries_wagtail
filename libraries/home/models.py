from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from blog.models import all_blog_posts
from instagram.models import Instagram
from hours.models import get_open_hours


class HomePage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.PROTECT,
        related_name='+',
        help_text='ideal dimensions are 1440x630px, please optimize image size too!',
    )
    # for search result template
    def _get_image(self):
        return self.background_image

    main_image = property(_get_image)

    # background_caption = RichTextField(blank=True)

    # blurbs for the 3 main sections (services, collections, about us)
    # we limit length & do not allow links like in a RichTextField
    latin = 'Aliquam iaculis ornare tristique. Phasellus ullamcorper tristique est, ac dictum quam sagittis ut.'
    services_text = models.CharField(default=latin, max_length=150)
    collections_text = models.CharField(default=latin, max_length=150)
    about_us_text = models.CharField(default=latin, max_length=150)

    # commented out are the actual, allowed subpages but they are singletons &
    # auto generated by migrations so we disable adding them here
    subpage_types = [
        # 'blog.BlogIndex',
        # 'categories.CategoryPage',
    ]

    # don't allow more home pages to be created
    parent_page_types = []

    content_panels = Page.content_panels + [
        ImageChooserPanel('background_image'),
        MultiFieldPanel([
            FieldPanel('services_text'),
            FieldPanel('collections_text'),
            FieldPanel('about_us_text'),
        ], heading="Category Descriptions")
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)

        # add latest 2 blog posts as "news items"
        news_items = all_blog_posts()[:2]
        context['news_items'] = news_items
        # pull open hours snippets for today
        context['hours'] = get_open_hours()

        # add instagram
        context['instagram'] = Instagram.objects.last()

        return context
