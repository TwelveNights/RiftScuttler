from django import forms


class AddDataTournament(forms.Form):
    id = forms.CharField(label='id', max_length=256)
    year = forms.IntegerField(min_value=0)
    location = forms.CharField(label='location', max_length=256)
    prize = forms.IntegerField(min_value=0)


class RemoveDataTournament(forms.Form):
    id = forms.CharField(label='id', max_length=256)
    year = forms.IntegerField(min_value=0)


class EditDataTournament(forms.Form):
    id = forms.CharField(label='id', max_length=256)
    year = forms.IntegerField(min_value=0)
    location = forms.CharField(label='location', max_length=256)
    prize = forms.IntegerField(min_value=0)