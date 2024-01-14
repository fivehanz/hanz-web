from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from wagtailseo.models import SeoMixin
from wagtailcache.cache import WagtailCacheMixin


class HomePage(WagtailCacheMixin, SeoMixin, Page):
    """ hero section fields """
    hero_primary_text = models.CharField(
        blank=True,
        max_length=100,
        verbose_name="Hero Primary Text (max 100 chars)",
        help_text="Homepage Primary Hero Text",
    )
    hero_secondary_text = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Hero Secondary Text (paragraph, max 255 chars)",
        help_text="Homepage Secondary Hero (paragraph) Text",
    )
    hero_primary_cta = models.CharField(
        blank=True,
        verbose_name="Hero Primary CTA",
        max_length=30,
        help_text="Homepage Hero Primary Call To Action Text",
    )
    hero_secondary_cta = models.CharField(
        blank=True,
        verbose_name="Hero Secondary CTA text",
        max_length=30,
        help_text="Homepage Hero Secondary Call To Action Text",
    )
    hero_primary_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero Primary CTA Link",
        help_text="Homepage Hero Primary CTA Link",
    )
    hero_secondary_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero Secondary CTA Link",
        help_text="Homepage Hero Secondary CTA Link",
    )

    # rest of the body content section fields
    body = RichTextField(blank=True)

    # panel definitions
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_primary_text"),
                FieldPanel("hero_secondary_text"),
            ],
            heading="hero section texts",
        ),
        MultiFieldPanel(
            [
                FieldPanel("hero_primary_cta"),
                FieldPanel("hero_primary_cta_link"),
            ],
            heading="hero primary CTA",
        ),
        MultiFieldPanel(
            [
                FieldPanel("hero_secondary_cta"),
                FieldPanel("hero_secondary_cta_link"),
            ],
            heading="hero secondary CTA",
        ),
        FieldPanel("body"),
    ]

    promote_panels = SeoMixin.seo_panels
