from django import forms
from app import models


class contact_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Message'}))

    class Meta:
        model = models.contact
        fields = "__all__"

class subcribe_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    class Meta:
        model = models.subcribe
        fields = "__all__"
