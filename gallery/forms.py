from django import forms
from django.forms.fields import CharField


class CommentForm(forms.Form):
    # author = CharField(
    #     max_length=60,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Your Name"
    #         }
    #     )
    # )
    body = CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Leave a  comment!"
            }
        )
    )
