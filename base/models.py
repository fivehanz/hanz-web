from django.db import models

# from modelcluster.models import ClusterableModel

from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)


@register_setting
class NavigationSettings(BaseGenericSetting):
    """ """

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
