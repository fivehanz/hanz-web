from wagtail.blocks import (
    CharBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StructBlock,
)

from wagtail.images.blocks import ImageChooserBlock
from base.blocks import BaseStreamBlock


class PostsBlock(StructBlock):
    heading = CharBlock()
    text = RichTextBlock(features=["bold", "italic", "link"], required=False)
    links = ListBlock(
        StructBlock(
            [
                ("name", CharBlock(max_length=100)),
                ("url", CharBlock()),
            ]
        )
    )
    page = PageChooserBlock(page_type=["blog.BlogPage"], required=False)

    class Meta:
        icon = "folder-open-inverse"


class ProjectsBlock(StructBlock):
    heading = CharBlock()
    text = RichTextBlock(features=["bold", "italic", "link"], required=False)
    image = ImageChooserBlock(required=False)
    featured = ListBlock(PostsBlock(required=True))

    class Meta:
        icon = "form"
        template = "project/blocks/projects.html"


class ProjectStreamBlock(BaseStreamBlock):
    projects = ProjectsBlock(group="Sections")
