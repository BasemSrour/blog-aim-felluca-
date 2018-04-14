import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


class Category(models.Model):
	category_name = models.CharField(max_length=100)

	def __str__(self):
		return "Category: " + self.category_name


class Article(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	article_title = models.CharField(max_length=100)
	article_content = models.TextField()
	article_pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('article_pub_date',)

	def was_published_recently(self):
		return self.article_pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	def __str__(self):
		return "Article: " + self.article_title


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	comment_content = models.CharField(max_length=1000)
	comment_pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('comment_pub_date',)

	def __str__(self):
		return self.comment_content
