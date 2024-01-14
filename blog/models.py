from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

from wagtailseo.models import SeoMixin
from wagtailcache.cache import WagtailCacheMixin


class BlogIndexPage(WagtailCacheMixin, SeoMixin, Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]
    promote_panels = SeoMixin.seo_panels


class BlogPage(WagtailCacheMixin, SeoMixin, Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    promote_panels = SeoMixin.seo_panels
