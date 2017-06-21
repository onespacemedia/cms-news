from cms.models import PageBaseSearchAdapter
from django.apps import AppConfig
from watson import search as watson


class NewsConfig(AppConfig):
    name = '{{ project_name }}.apps.news'

    def ready(self):
        Article = self.get_model('Article')
        watson.register(Article, adapter_cls=PageBaseSearchAdapter)
