__author__ = 'Stephen'
from django.template import Library

register = Library()

@register.filter(name='split')
def split(value, at):
    # split the string into a list

    return value.split(at) if value else ""

