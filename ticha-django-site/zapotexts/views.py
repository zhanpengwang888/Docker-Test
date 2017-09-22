"""This module implements the views for the Ticha site."""
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import MultipleObjectsReturned

from haystack.generic_views import SearchView

import contextlib
from lxml import etree, sax
from .ticha_magic import ticha_magic

from .models import PrintedText, Page
from .forms import ImportXMLForm


import logging
logger = logging.getLogger('ticha')


def landing(request):
    return render(request, 'zapotexts/landing.html')


def levanto_redirect(request):
    return document_viewer(request, 'levanto', '4')


def document_viewer(request, slug, page='0', mode=''):
    """The view for the JavaScript-powered document viewer.

    This replaces the page_detail_view. The mode keyword argument is kept for backwards 
    compatability with the page_detail_view URLs.
    """
    doc = PrintedText.objects.get(slug=slug)
    payload = {'text_name': repr(doc.title.lower()), 'this_page': int(page),
               'last_page': doc.last_page}
    if doc.zoomable:
        return render(request, 'zapotexts/viewer_zoomable.html', payload)
    else:
        return render(request, 'zapotexts/viewer_regular.html', payload)


def page_detail_view(request, slug, page, mode):
    """The view for an individual Page of a PrintedText manuscript.

    This has been deprecated by the document_viewer view.
    """
    # this code needs to be changed to handle a MultipleObjects error
    doc = PrintedText.objects.get(slug=slug)
    page_obj = Page.objects.get(man=doc, linear_page_number=page)

    # compute the next and previous page numbers
    # '9999' is the default, which will cause the button to be disabled
    prev_page, next_page = '9999', '9999'
    if page != str(doc.last_page):
        next_page = int(page) + 1
    if page != '0':
        prev_page = int(page) - 1

    img_url = 'zapotexts/img/printed_manuscripts/%s/%s.jpg' % (doc.slug, page)
    context = {'page': page_obj, 'doc_slug': slug, 'prev_page': prev_page, 'next_page': next_page,
               'last_page': doc.last_page, 'img_url': img_url, 'mode': mode}
    return render(request, 'zapotexts/page_detail.html', context)


def page_download_view(request, slug, page, mode):
    doc = PrintedText.objects.get(slug=slug)
    page = Page.objects.get(man=doc, linear_page_number=page)
    if mode == 'original':
        return HttpResponse(page.transcription)
    elif mode == 'regular':
        return HttpResponse(page.transcription_regular)
    elif mode == 'workshop':
        return HttpResponse(page.workshop_notes)
    else:
        return HttpResponse('')


class CustomSearchView(SearchView):
    """The view for the Haystack search."""
    pass


def AdminDictionary(request):
    return render(request, 'admin/dictionary/index.html')


def admin_import_xml(request): 
    if request.method == 'POST':
        form = ImportXMLForm(request.POST, request.FILES)
        if form.is_valid():
            import_xml_from_file(form.cleaned_data['document'], request.FILES['xml_file'],
                                 request.FILES.get('flex_file'))
            return HttpResponseRedirect('/admin/')
    else:
        form = ImportXMLForm()
    return render(request, 'zapotexts/import_xml.html', {'form': form})


def import_xml_from_file(doc, xml_file, flex_file):
    """Convert the XML file to HTML and save each page as a Page object."""
    logger.debug('import_xml_from_file: Uploading XML transcription for %s', doc.title)
    xml_data = xml_file.read()
    try:
        xml_root = etree.XML(xml_data)
    except etree.XMLSyntaxError as e:
        logger.error('import_xml_from_file: %s', e)
        return
    xml_kwargs = {'spellchoice': 'orig', 'abbrchoice': 'abbr', 'textname': doc.title.lower()}
    if flex_file:
        logger.debug('import_xml_from_file: FLEx upload found')
        flex_data = flex_file.read().decode('utf-8')
    else:
        logger.debug('import_xml_from_file: No FLEx upload')
        flex_data = None
    try:
        html_tree = ticha_magic.xml_to_html(xml_root, flex_data=None, **xml_kwargs)
    except sax.SaxError as e:
        logger.error('PrintedText.save: %s', e)
    else:
        for i, elem in enumerate(html_tree.getroot()):
            with contextlib.suppress(MultipleObjectsReturned):
                page, _ = doc.page_set.get_or_create(man=doc, linear_page_number=i)
                page.transcription = etree.tostring(elem, encoding='unicode', method='html')
                page.transcription_regular = ''
                page.page_id = elem.attrib.get('data-rvn', '')
                page.save()
        doc.last_page = i
    logger.debug('import_xml_from_file: Successfully saved %s', doc.title)
    doc.save()
