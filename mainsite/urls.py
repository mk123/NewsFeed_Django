from django.urls import path
from mainsite.views import index, news_for_category

app_name = "mainsite"

urlpatterns = [
    path('index', index, name='index'),
    path('category/<int:category_id>',news_for_category, name='category_news'),
]
