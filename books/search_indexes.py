from haystack import indexes

from books.models import Page


class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    page_number = indexes.CharField(model_attr='page_number')
    body = indexes.CharField(model_attr='body')
    node = indexes.CharField(model_attr='node')

    def get_model(self):
        return Page

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
