from django import template


register = template.Library()

def typeadmin(value):

    if value == 'policeadmin':
        return "/admin-validate/"
    elif value == 'superadmin':
        return "/sadmin-validate/"
    return "/login.html/"

register.filter('typeadmin',typeadmin)
