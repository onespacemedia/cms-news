from django.contrib import admin
from django.test import TestCase

from ..models import Article, Category

import sys
import mock


class TestArticleAdminBase(TestCase):

    def test_article_admin(self):
        module = sys.modules['{{ project_name }}.apps.news.admin']
        del sys.modules['{{ project_name }}.apps.news.admin']

        admin.site.unregister(Article)
        admin.site.unregister(Category)

        with mock.patch('{{ project_name }}.apps.news.admin.externals.reversion', new=False):
            from ..admin import ArticleAdmin, ArticleAdminBase
            assert ArticleAdmin
            self.assertIs(ArticleAdmin.__bases__[0], ArticleAdminBase)
            self.assertEqual(len(ArticleAdmin.__bases__), 1)

        sys.modules['{{ project_name }}.apps.news.admin'] = module
