from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.search.index import SearchField
from wagtailseo.models import SeoMixin
from wagtailcache.cache import WagtailCacheMixin

from project.blocks import ProjectStreamBlock


class ProjectPage(WagtailCacheMixin, SeoMixin, Page):
    parent_page_types = ["home.HomePage"]

    body = StreamField(
        ProjectStreamBlock(),
        blank=True,
        use_json_field=True,
        help_text="Use this section to list your projects and skills.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Project Page"
        verbose_name_plural = "Project Pages"

    promote_panels = SeoMixin.seo_panels

    search_fields = Page.search_fields + [
        SearchField("body"),
    ]
