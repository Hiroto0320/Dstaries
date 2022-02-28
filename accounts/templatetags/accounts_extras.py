from django import template

register = template.Library()

@register.filter
def join(arg1, arg2):
    i = arg2*3
    j = int(i/2)
    return str(arg1) + str(j) + '.png'