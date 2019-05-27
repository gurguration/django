from django import forms


class MyForm(forms.Form):
    text = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'Enter todo here. E.G delete completed',
        'class': 'form-control',
        'area-label': 'Todo',
        'area-describeby': 'add-btn',
        }
        ))
