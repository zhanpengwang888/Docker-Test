"""This module defines the database models used by the Ticha site internally. Currently, three
   models exist:

       HandwrittenText: a model for handwritten documents that includes a large amount of metadata
                        in English and Spanish.

       PrintedText: a model for printed documents that includes a transcription of the document as
                    an XML file.

       Page: a model for the individual pages of the printed documents, which includes a
             transcription of the page as a text field.
"""
import requests

from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse  # for get_absolute_url


import logging
logger = logging.getLogger('ticha')


class PrintedText(models.Model):
    """A model representing a printed manuscript."""
    title = models.CharField(max_length=50, unique=True)
    last_page = models.IntegerField(default=0)
    slug = models.SlugField()
    citation = models.TextField(blank=True)
    zoomable = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Fill the slug field using the title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Page(models.Model):
    """A model representing a page of a Printed manuscript."""
    transcription = models.TextField(blank=True)
    transcription_regular = models.TextField(verbose_name='Regular Transcription', blank=True)
    workshop_notes = models.TextField(verbose_name='Workshop Notes', blank=True)
    man = models.ForeignKey(PrintedText, on_delete=models.CASCADE, verbose_name='Text')
    # page_id is the actual page number used in the book (1r, 2v etc.)
    # NOTE: the page_id of a Page is not necessarily unique for a given PrintedText object; some
    # (like Arte) have duplicate page numbers. If you need a unique ID for a Page of a given
    # PrintedText object, use the linear_page_number field instead.
    page_id = models.CharField(max_length=10, blank=True, default='', verbose_name='Page ID')
    linear_page_number = models.IntegerField()

    def get_absolute_url(self):
        return reverse('zapotexts:page_detail',
                       args=[self.man.slug, self.linear_page_number, 'original'])

    def __str__(self):
        return 'Page ' + str(self.page_id) + ' of ' + self.man.title

    class Meta:
        verbose_name = 'Printed text page'
