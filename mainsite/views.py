from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from mainsite.models import Article, ArticleCategory
# Create your views here.

def index(request):
	articles = Article.objects.all().order_by('-id')[0:10]
	categories = ArticleCategory.objects.all()
	page = loader.get_template("mainsite/index.html")
	context = {
	"articles": articles,
	"categories": categories,
	"page_title": "Home page"
	}
	return HttpResponse(page.render(context, request))

def news_for_category(request, category_id):
	category = ArticleCategory.objects.get(id=category_id)
	articles = Article.objects.filter(category=category)
	categories = ArticleCategory.objects.all()
	page = loader.get_template("mainsite/index.html")
	context = {
	"articles": articles,
	"categories": categories,
	"page_title": category.name
	}
	return HttpResponse(page.render(context, request))
