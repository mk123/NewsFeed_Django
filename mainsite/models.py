from django.db import models

# Create your models here.

class ArticleCategory(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Article(models.Model):
	category = models.ForeignKey(ArticleCategory, on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length=400)
	content = models.TextField()


	def __str__(self):
		return self.title
		

