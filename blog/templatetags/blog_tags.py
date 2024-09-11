from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


""" Для того чтобы быть допустимой библиотекой тегов, в каждом содержащем шаблонные теги модуле должна быть 
определена переменная с именем register."""
register = template.Library()  # для регистрации шаблонных тегов и фильтров приложения.


"""В приведенном выше исходном коде тег total_posts был определен с помощью простой функции Python. 
В функцию был добавлен декоратор @register.simple_tag, чтобы зарегистрировать ее как простой тег."""
@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).exclude(total_comments=0).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))