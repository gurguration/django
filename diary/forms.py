from django.forms import ModelForm,Textarea
from django import forms
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text',)
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20,'class':'textarea',
                                    'placeholder': "What's Up?"}),
        }