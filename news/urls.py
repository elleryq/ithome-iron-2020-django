# news/urls.py
from news.viewsets import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
urlpatterns = router.urls
