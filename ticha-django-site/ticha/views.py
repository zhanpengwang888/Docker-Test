from django.shortcuts import render, render_to_response
from django.template import RequestContext


def index(request): return render(request, 'ticha/index.html')
def about(request): return render(request, 'ticha/about.html')
def team(request): return render(request, 'ticha/team.html')
def acknowledgements(request): return render(request, 'ticha/acknowledgements.html')
def linguistic(request): return render(request, 'ticha/linguistic.html')
def context(request): return render(request, 'ticha/context.html')
def arte(request): return render(request, 'ticha/arte.html')
def sample_arte(request): return render(request, 'ticha/sample_arte.html')
def doctrina(request): return render(request, 'ticha/doctrina.html')
def feria(request): return render(request, 'ticha/feria.html')
def sample_doctrina(request): return render(request, 'ticha/sample_doctrina.html')
def handwritten(request): return render(request, 'ticha/handwritten.html')
def sample_handwritten(request): return render(request, 'ticha/sample_handwritten.html')
def timeline(request): return render(request, 'ticha/timeline.html')
def bibliography(request): return render(request, 'ticha/bibliography.html')
def arte_pdf(request): return render(request, 'ticha/arte_pdf.html')
def levanto_outline(request): return render(request, 'ticha/levanto_outline.html')
def arte_outline(request): return render(request, 'ticha/arte_outline.html')
def arte_original(request): return render(request, 'ticha/arte_original.html')
def reg_spanish(request): return render(request, 'ticha/reg_spanish.html')
def doctrina_pdf(request): return render(request, 'ticha/doctrina_pdf.html')
def form(request): return render(request, 'ticha/form.html')
def resources(request): return render(request, 'ticha/resources.html')


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
