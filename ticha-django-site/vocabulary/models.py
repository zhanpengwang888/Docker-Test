import requests
import time
import html
from lxml import etree
from lxml.builder import E

from django.db import models
from django.core.urlresolvers import reverse, NoReverseMatch


import logging
logger = logging.getLogger('ticha')


class PageIndex(models.Model):
    contents = models.TextField()
    reverse_index = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.paginate_dictionary()
        self.fix_reverse_index()
        super().save(*args, **kwargs)

    def paginate_dictionary(self):
        tree = etree.HTML(self.contents)
        start = 0
        this_letter = None
        current_div = etree.Element('div')
        Page.objects.filter(parent=self).delete()
        Word.objects.all().delete()
        for i, entry in enumerate(tree[0]):
            if entry.get('class') == 'letHead':
                if this_letter is not None:
                    div_str = etree.tostring(current_div).decode('utf-8')
                    self.page_set.create(letter=this_letter, contents=div_str)
                this_letter = entry[0].text.split()[0]
                start = i + 1
                current_div = etree.Element('div')
            else:
                # Create Word objects for searching
                words = entry.xpath('span[@class = "headword"]//text()')
                if words:
                    Word.objects.create(word=words[0], html_id=entry.get('id', ''))
                czis = entry.xpath('span[@class = "czi"]//text()')
                if czis:
                    # This is what ultimately gets inserted:
                    # <div class="audio-div">
                    #   <p>Hear it in {{DIALECT}}: <b>{{WORD}}</b>
                    #      <img class="play-button">
                    #      <a href="{{LINK TO DICTIONARY}}"><img></a>
                    #   </p>
                    #   ... (potentially several of these <p>s)
                    # </div>
                    headwords_dialects_and_urls = self.fetch_metadata_from_czi(czis[0])
                    audio_div = E.div({'class': 'audio-div'})
                    for headword, dialect, url, dict_url in headwords_dialects_and_urls:
                        audio_attrs = {
                          'class': 'play-button',
                          'src': '/static/zapotexts/img/play_button.png',
                          'data-url': url,
                        }
                        audio = E.img(audio_attrs)
                        if dialect:
                            text = 'Hear it in ' + dialect + ': '
                        else:
                            text = 'Hear it in a modern dialect: '
                        anchor = E.a(E.img(src='/static/zapotexts/img/forward_arrow.png'),
                                     href=dict_url, target='_blank')
                        audio_div.append(E.p(text, E.b(html.unescape(headword)), audio, anchor))
                    if len(audio_div) > 0:
                        entry.append(audio_div)
                    # don't want to overwhelm the talking dictionaries API
                    time.sleep(0.25)
                current_div.append(entry)

    def fix_reverse_index(self):
        """Fix the URLs in the reverse index."""
        tree = etree.HTML(self.reverse_index)
        for i, entry in enumerate(tree[0]):
            if entry.get('class') != 'letHead':
                for anchor in entry.xpath('.//a'):
                    urlhash = anchor.get('href')
                    letter = anchor.text[0].upper()
                    # Some words begin with a dash or an equals sign
                    if not letter.isalpha() and len(anchor.text) >= 2:
                        letter = anchor.text[1].upper()
                    try:
                        root_url = reverse('vocabulary:index', args=[letter])
                    except NoReverseMatch:
                        logger.error('No match for vocabulary index, letter %s', letter)
                    else:
                        anchor.attrib['href'] = root_url + urlhash
        self.reverse_index = etree.tostring(tree, encoding='unicode')

    @staticmethod
    def fetch_metadata_from_czi(czi):
        payload = {'czi': czi, 'export': 'json', 'return': 'all'}
        r = requests.get('http://talkingdictionary.swarthmore.edu/teotitlan/czi/', params=payload)
        try:
            data = r.json()
        except ValueError:
            logger.error('Bad JSON on API return from CZI %s', czi)
            return set()
        return set((x.get('lang'), x.get('language_name'), x.get('audio'), x.get('dict_url'))
                   for x in data)

    class Meta:
        verbose_name_plural = 'dictionaries'


class Page(models.Model):
    letter = models.CharField(max_length=2)
    contents = models.TextField()
    parent = models.ForeignKey('PageIndex', on_delete=models.CASCADE)

    def __str__(self):
        return 'Page ' + self.letter

    def get_absolute_url(self):
        return reverse('vocabulary:index', args=[self.letter])


class Word(models.Model):
    word = models.CharField(max_length=50)
    html_id = models.CharField(max_length=50)

    def __str__(self):
        return 'Word "{}"'.format(self.word)

    def get_absolute_url(self):
        return reverse('vocabulary:index', args=[self.word[0].upper()]) + '#' + self.html_id
