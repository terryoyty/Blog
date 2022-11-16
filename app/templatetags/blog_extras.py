from django import template
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('app/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    if context.request.user.is_authenticated:
        user = context.request.user
    else:
        user = get_object_or_404(User, pk=2)
    return {
        'recent_post_list': user.post_set.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('app/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    if context.request.user.is_authenticated:
        user = context.request.user
    else:
        user = get_object_or_404(User, pk=2)
    return {
        'date_list': user.post_set.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('app/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    if context.request.user.is_authenticated:
        user = context.request.user
    else:
        user = get_object_or_404(User, pk=2)
    category_set = set()
    for post in user.post_set.all():
        category_set.add(post.category)
    return {
        'category_list': category_set,
    }


@register.inclusion_tag('app/inclusions/_tags.html', takes_context=True)
def show_tags(context, post=None):
    if not post:
        if context.request.user.is_authenticated:
            user = context.request.user
        else:
            user = get_object_or_404(User, pk=2)

        tag_list = Tag.objects.filter(post__author=user)
        name = '标签云'
    else:
        tag_list = post.tags.all()
        name = '标签'

    return {
        'tag_list': tag_list,
        'name': name
    }