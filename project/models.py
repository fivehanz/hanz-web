from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from project.blocks import ProjectStreamBlock


class ProjectPage(Page):
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
