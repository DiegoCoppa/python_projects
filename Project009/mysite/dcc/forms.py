# -*- coding: utf-8 -*-

from django import forms

from .models import XmlDocuments

class NameForm(forms.Form):
    user = forms.CharField(label='User', max_length=100)


class DocumentFormXml(forms.ModelForm):
    class Meta:
        model = XmlDocuments
        fields = ('id', 'description', 'xmldocument', 'dcc_user',)
        #Acá no va uploaded_at por que no es un campo editable
   
    """   
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    """