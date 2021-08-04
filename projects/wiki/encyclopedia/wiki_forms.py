from django import forms

class NewPage(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(label=False)
