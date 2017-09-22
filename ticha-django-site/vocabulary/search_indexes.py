from haystack import indexes
from .models import Word


class WordIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    word = indexes.CharField(model_attr='word')

    def get_model(self):
        return Word
