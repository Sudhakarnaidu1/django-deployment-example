from django import template

register=template.Library()


def cut(value,arg):
    return value.replace(arg,'')
register.filter('cut',cut)


def multiply(value,arg):
    return value*arg
register.filter('multiply',multiply)


def floor(value,arg):
    return value//arg
register.filter('floordiv',floor)


@register.filter('fun1')
def fun1(value):
    return value.lower()


def repla(value,*arg):
    return value.replace('HELLO',arg)
register.filter('repla',repla)