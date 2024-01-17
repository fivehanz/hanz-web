from django.db import models
from modelcluster.models import ParentalKey

from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    # PublishingPanel,
)

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

# from wagtail.contrib.forms.panels import FormSubmissionsPanel

from wagtail.contrib.settings.models import BaseGenericSetting, BaseSiteSetting, register_setting

# from wagtail.snippets.models import register_snippet

from wagtail.fields import RichTextField

# from wagtail.models import (
#     DraftStateMixin,
#     PreviewableMixin,
#     RevisionMixin,
#     TranslatableMixin,
# )


@register_setting
class NavigationSettings(BaseGenericSetting):
    """settings for navigation"""

    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),  # Panel for Twitter URL field
                FieldPanel("github_url"),  # Panel for GitHub URL field
                FieldPanel("linkedin_url"),  # Panel for LinkedIn URL field
            ],
            "Social settings",  # Title of the multi-field panel
        )
    ]


@register_setting
class GoogleTagManagerSettings(BaseSiteSetting):
    """ google tag manager id settings """

    class Meta:
        verbose_name = "Google Tag Manager"

    google_tag_manager_id = models.CharField(
        verbose_name="Google Tag Manager ID",
        max_length=255,
        blank=True,
        help_text='Begins with "GTM-"',
    )

    panels = [
        FieldPanel("google_tag_manager_id"),
    ]


class FormField(AbstractFormField):
    page = ParentalKey(
        "FormPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        FieldPanel("thank_you_text"),
        InlinePanel("form_fields", label="Form fields"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("to_address", classname="col6"),
                        FieldPanel("from_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]
