from django import template
from phil.models import *

register = template.Library()



@register.simple_tag(name='book_list')
def book_list():
    return Books.objects.all()

@register.simple_tag(name='text_list')
def text_list():
    return Articles.objects.all()

@register.simple_tag(name='measurments')
def measurments_list():
    return Measurments.objects.all()

@register.inclusion_tag('phil/soft_skills.html')
def empty():
    return 1
