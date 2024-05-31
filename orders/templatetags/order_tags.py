from django import template

register = template.Library()

@register.filter
def is_freelancer(user):
    return hasattr(user, 'freelancer_profile')

@register.filter
def is_client(user):
    return hasattr(user, 'client_profile')
