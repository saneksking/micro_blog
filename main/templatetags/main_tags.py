from django import template
from main.models import SiteSettings

register = template.Library()


@register.simple_tag
def main_settings():
    return SiteSettings.objects.last()
