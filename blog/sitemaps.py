from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    """Определили конкретно-прикладную карту сайта
    Атрибуты changefreq и priority указывают частоту изменения страниц
    постов и их релевантность на веб-сайте (максимальное значение равно 1)"""
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated