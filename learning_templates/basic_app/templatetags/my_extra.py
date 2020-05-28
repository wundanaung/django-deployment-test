from django import template

register = template.Library()

@register.filter(name='rword')
def rword(value,arg):
    """
    This removes arg from values
    """
    return value.replace(arg,'')

#have used decorators above instead of thisregister.filter('rword',rword)
