from django.contrib import admin

from .models import PrintedText, Page


class PrintedTextAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'citation', 'zoomable')


class PageAdmin(admin.ModelAdmin):
    exclude = ('linear_page_number',)


admin.site.register(PrintedText, PrintedTextAdmin)
admin.site.register(Page, PageAdmin)
