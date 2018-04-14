from django.conf.urls import url, include
#from django.urls import path
from rest_framework.routers import DefaultRouter
from blog_aim_felluca import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='blog_aim_felluca')

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
		url(r'^', include(router.urls)),
		url(r'^schema/$', schema_view)
]
