from django import forms


class DiscountApllyForm(forms.Form):
    _ფასდაკლების_პროცენტი = forms.IntegerField(max_value=100, min_value=0)
