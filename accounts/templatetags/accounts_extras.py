from django import template

register = template.Library()

@register.filter
def join(arg1, arg2):
    return str(arg1) + str(arg2) + '.png'

@register.filter
def stories_is_max(arg1):
    if arg1>=300:
        return False
    else:
        return True