from django import forms

"""
References:
https://jacobian.org/writing/dynamic-form-generation/
"""


class AccessFormInput(forms.Form):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        self.req = kwargs.pop('req', None)
        super(AccessFormInput, self).__init__(*args, **kwargs)
        for attribute in extra:
            if attribute[1].find("charfield") != -1:
                self.fields['%s' % attribute[0]] = forms.CharField(label=attribute[0], max_length=attribute[1][9:])
            elif attribute[1] == 'text':
                self.fields['%s' % attribute[0]] = forms.CharField(label=attribute[0], max_length=1000)
            elif attribute[1] == 'int':
                self.fields['%s' % attribute[0]] = forms.IntegerField(label=attribute[0], min_value=0)
            elif attribute[1] == 'datetime':
                self.fields['%s' % attribute[0]] = forms.DateTimeField(label=attribute[0])
            elif attribute[1] == 'boolean':
                self.fields['%s' % attribute[0]] = forms.IntegerField(label=attribute[0], min_value=0, max_value=1)
            elif attribute[1] == 'date':
                self.fields['%s' % attribute[0]] = forms.DateField(label=attribute[0])
            abs_url = self.req.get_full_path()
            if abs_url.find("/add_") != -1 or abs_url.find("/edit_") != -1:
                if attribute[2] == "pk":
                    self.fields['%s' % attribute[0]].widget.attrs.update({
                        "class": "pk",
                        "placeholder": "<Primary Key>"
                    })
                else:
                    self.fields['%s' % attribute[0]].widget.attrs.update({
                        "class": "non-pk",
                    })
            if abs_url.find("/edit_") != -1:
                if attribute[2] == "non-pk":
                    self.fields['%s' % attribute[0]].required = False

    def extra_attributes(self):
        for name, value in self.cleaned_data.items():
            yield (self.fields[name].label, value)
