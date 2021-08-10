from django import forms

class NewPage(forms.Form):
    title = forms.CharField(label="Title", max_length=100, error_messages={'required': 'Please The title of the topic'})
    content = forms.CharField(widget=forms.Textarea, label=False)


class EditEntry(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label=False)
