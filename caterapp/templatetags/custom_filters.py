from django import template

register = template.Library()


@register.filter(name='wow_delay')
def wow_delay(counter, delay):
    return f'{counter * delay:.1f}'
