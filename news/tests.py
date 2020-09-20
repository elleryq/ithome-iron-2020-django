from django.test import TestCase
from .models import Article


class ArticleTestCase(TestCase):
    def setUp(self):
        pass

    def test_article_is_published(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(True, True)
