from django import forms


class AddData(forms.Form):
    id = forms.CharField(label='id', max_length=256)
    year = forms.IntegerField(min_value=0)
    location = forms.CharField(label='location', max_length=256)
    prize = forms.IntegerField(min_value=0)

