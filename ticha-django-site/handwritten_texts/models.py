from django.db import models
from django.core.urlresolvers import reverse  # for get_absolute_url


class HandwrittenText(models.Model):
    """A model representing a handwritten manuscript."""
    title = models.CharField(max_length=100, default='')
    título = models.CharField(max_length=100, default='')
    language = models.CharField(max_length=50, default='')
    idioma = models.CharField(max_length=50, default='')
    document_type = models.CharField(max_length=50, default='')
    tipo_del_documento = models.CharField(max_length=50, default='')
    material_type = models.CharField(max_length=50, default='', blank=True)
    archive = models.CharField(max_length=100, default='', blank=True)
    archivo = models.CharField(max_length=100, default='', blank=True)
    collection = models.CharField(max_length=100, default='', blank=True)
    colección = models.CharField(max_length=100, default='', blank=True)
    call_number = models.CharField(max_length=100, default='', blank=True)
    número_de_etiqueta = models.CharField(max_length=100, default='', blank=True)
    page = models.CharField(max_length=50, default='', blank=True)
    páginas = models.CharField(max_length=50, default='', blank=True)
    date_digitized = models.DateField(null=True, blank=True)
    year = models.CharField(max_length=10, default='', blank=True)
    town_modern_official = models.CharField(max_length=100, default='', blank=True,
                                            verbose_name='Town (Modern Official)')
    pueblo = models.CharField(max_length=100, default='', blank=True)
    primary_parties = models.CharField(max_length=300, default='', blank=True)
    personajes_principales = models.CharField(max_length=300, default='', blank=True)
    slug = models.SlugField(verbose_name='Ticha ID')
    town_short = models.CharField(max_length=50, default='', blank=True,
                                  verbose_name='Town (Short)')
    date = models.CharField(max_length=50, default='', blank=True)
    fecha = models.CharField(max_length=50, default='', blank=True)
    has_translation = models.CharField(max_length=50, default='', blank=True)
    transcription = models.TextField(blank=True)
    scribe = models.CharField(max_length=100, default='', blank=True)
    escribano = models.CharField(max_length=100, default='', blank=True)
    is_translation = models.CharField(max_length=50, default='', blank=True)
    witnesses = models.CharField(max_length=300, default='', blank=True)
    testigos = models.CharField(max_length=300, default='', blank=True)
    acknowledgements = models.TextField(default='', blank=True)
    agradecimientos = models.TextField(default='', blank=True)
    permission_file = models.URLField(default='', blank=True)
    percent_needs_review = models.CharField(max_length=50, default='', blank=True)
    requester_project = models.CharField(max_length=50, default='', blank=True,
                                         verbose_name='Requester/Project')
    omeka_id = models.CharField(max_length=10, default='', blank=True, verbose_name='Omeka ID')
    timeline_media_thumbnail = models.CharField(max_length=100, default='', blank=True)
    timeline_text = models.TextField(default='', blank=True)
    timeline_headline = models.CharField(max_length=50, default='', blank=True)
    timeline_start_date = models.CharField(max_length=50, default='', blank=True)
    interlinear_analysis = models.TextField(default='', blank=True)
    timeline_spanish_text = models.TextField(default='', blank=True)
    timeline_spanish_headline = models.CharField(max_length=50, default='', blank=True)

    def get_absolute_url(self):
        if self.slug:
            return reverse('handwritten_texts:detail', args=[self.slug])
        else:
            return reverse('handwritten_texts:list')

    def __str__(self):
        return self.title
