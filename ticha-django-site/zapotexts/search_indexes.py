"""This module defines the search indexes used by the Haystack app."""
from haystack import indexes
from zapotexts.models import PrintedText, Page


class PrintedTextIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return PrintedText


class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    transcription = indexes.CharField(model_attr='transcription')
    page_id = indexes.CharField(model_attr='page_id')

    def get_model(self):
        return Page
