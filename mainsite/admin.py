from django.contrib import admin

from mainsite.models import ArticleCategory, Article

admin.site.register([Article, ArticleCategory])
