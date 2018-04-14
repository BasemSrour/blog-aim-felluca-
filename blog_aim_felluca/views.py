from blog_aim_felluca.models import Category, Article, Comment
from blog_aim_felluca.serializers import CategorySerializer, ArticleSerializer, CommentSerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all().order_by('-article_pub_date')
	serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all().order_by('-comment_pub_date')
	serializer_class = CommentSerializer
