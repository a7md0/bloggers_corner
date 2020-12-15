from django import forms

class ContactusForm(forms.Form):
    name = forms.CharField(max_length=60)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
