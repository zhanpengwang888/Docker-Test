from django import forms

from .models import PrintedText


class ImportXMLForm(forms.Form):
    document = forms.ModelChoiceField(queryset=PrintedText.objects.all())
    xml_file = forms.FileField(label='XML file')
    flex_file = forms.FileField(label='FLEx export', required=False)
