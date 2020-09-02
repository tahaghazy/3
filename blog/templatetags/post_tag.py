from django import template
from blog.models import Post,Category
from django.shortcuts import render,get_object_or_404


register = template.Library()

@register.inclusion_tag('latest_posts.html')
def latest_posts():

    context = {
        'l_posts': Post.objects.filter(active=True)[0:10],
    }
    return context

@register.inclusion_tag('category.html')
def Category():

    context = {
        'Categories': Category.objects.all(),
    }
    return context

