from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.now().strftime(format_string)


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    dates = context['request'].GET.copy()
    for key, value in kwargs.items():
        dates[key] = value
    return dates.urlencode()
