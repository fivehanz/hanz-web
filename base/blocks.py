from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
)

from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "base/blocks/image.html"


class HeadingBlock(StructBlock):
    heading = CharBlock(required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading.html"


class BaseStreamBlock(StreamBlock):
    heading = HeadingBlock(required=False)
    paragraph = RichTextBlock(icon="pilcrow", required=False)
    image = ImageBlock(required=False)
    embed = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        icon="media",
        required=False,
    )
