from django import forms

class DataForm(forms.Form):
    data = forms.CharField(label='Enter your data', max_length=255)
