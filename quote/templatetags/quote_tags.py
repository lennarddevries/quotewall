from django import template

register = template.Library()

@register.filter
def previous(value, quotes):
    if value.get('first'):
        return quotes.count()
    return value.get('counter') - 1

@register.filter
def next(value):
    if value.get('last'):
        return 1
    return value.get('counter') + 1
