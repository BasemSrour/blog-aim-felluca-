from rest_framework import serializers
from blog_aim_felluca.models import Category, Article, Comment


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'category_name')


class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ('id', 'category', 'article_title', 'article_content', 'article_pub_date')


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'article', 'comment_content', 'comment_pub_date')
