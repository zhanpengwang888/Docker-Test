from django.shortcuts import render

from .models import PageIndex, Page


def index(request, letter='A'):
    all_pages = Page.objects.order_by('letter')
    dct = PageIndex.objects.all()[0]
    page = Page.objects.get(letter=letter)
    context = {'pages': all_pages, 'dct': dct, 'page': page}
    return render(request, 'vocabulary/index.html', context=context)


def reverse_index(request):
    all_pages = Page.objects.order_by('letter')
    dct = PageIndex.objects.all()[0]
    context = {'pages': all_pages, 'dct': dct}
    return render(request, 'vocabulary/reverse_index.html', context)
