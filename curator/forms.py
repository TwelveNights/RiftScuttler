from django import forms

# References:
# https://jacobian.org/writing/dynamic-form-generation/
# fix different character limits (Not all 256)


class AccessFormInput(forms.Form):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(AccessFormInput, self).__init__(*args, **kwargs)

        for attribute in extra:
            if attribute[1] == 'charfield2':
                self.fields['%s' % attribute[0]] = forms.CharField(label=attribute[0], max_length=2)
            elif attribute[1] == 'charfield6':
                self.fields['%s' % attribute[0]] = forms.CharField(label=attribute[0], max_length=6)
            elif attribute[1] == 'charfield10':
                self.fields['%s' % attribute[0]] = forms.CharField(label=attribute[0], max_length=10)
            elif attribute[1] == 'charfield16':
                self.fields['%s' % attribute[0]] = forms.CharField(label=attribute[0], max_length=16)
            elif attribute[1] == 'charfield64':
                self.fields['%s' % attribute[0]] = forms.CharField(label=attribute[0], max_length=64)
            elif attribute[1] == 'charfield256':
                self.fields['%s' % attribute[0]] = forms.CharField(label=attribute[0], max_length=256)
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

    def extra_attributes(self):
        for name, value in self.cleaned_data.items():
            yield (self.fields[name].label, value)
