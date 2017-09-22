from django.shortcuts import render

from .models import HandwrittenText
from django.views.generic import ListView


class HandwrittenListView(ListView):
    model = HandwrittenText
    template_name = 'handwritten_texts/list.html'


EN_TO_ES = {
  'title': 'título', "language": "idioma", "document_type": "tipo_del_documento",
  "material_type": "material_type", "archive": "archivo", "collection": "colección",
  "call_number": "número_de_etiqueta", "page": "páginas", "date_digitized": "date_digitized",
  "year": "year", "town_modern_official": "pueblo", "primary_parties": "personajes_principales",
  "slug": "slug", "town_short": "town_short", "date": "fecha", "has_translation": "has_translation",
  "transcription": "transcription", "scribe": "escribano", "is_translation": "is_translation",
  "witnesses": "testigos", "acknowledgements": "agradecimientos",
  "permission_file": "permission_file", "percent_needs_review": "percent_needs_review",
  "requester_project": "requester_project", "timeline_text": "timeline_spanish_text",
  "timeline_headline": "timeline_spanish_headline"
}
def handwritten_text_detail_view(request, slug):
    """Custom view to supply the HandwrittenText detail template with its
       fields in the proper language.
    """
    man = HandwrittenText.objects.get(slug=slug)
    translated_man = {}
    for en_key, es_key in EN_TO_ES.items():
        if request.LANGUAGE_CODE == 'es':
            try:
                translated_man[en_key] = getattr(man, es_key)
            except AttributeError:
                translated_man[en_key] = getattr(man, en_key)
        else:
            translated_man[en_key] = getattr(man, en_key)
    context = {'man': translated_man, 'omeka_id': man.omeka_id}
    return render(request, 'handwritten_texts/detail.html', context)


def redirect_view(request):
    return render(request, 'handwritten_texts/redirect.html')
