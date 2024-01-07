from django import template
from django.http import HttpRequest
from typing import Any

from wagtail.models import Site


register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context: dict[str, Any]) -> Any:
    """
    Retrieve the root page for the current site.

    Args:
        context: The context dictionary containing the request.

    Returns:
        The root page for the current site.
    """
    request: HttpRequest = context["request"]
    site: Site | Any = Site.find_for_request(request)
    root_page: Any = site.root_page
    return root_page
