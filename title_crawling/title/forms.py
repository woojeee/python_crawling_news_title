from django import forms
from .models import SearchTitle

class SearchTitleForm(forms.ModelForm):
    class Meta:
        model = SearchTitle
        fields = ('words',)