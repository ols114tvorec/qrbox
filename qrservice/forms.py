from django import forms

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"autofocus": "", "placeholder": "Опиши свой визит к нам"}))
    qr_id = forms.CharField(widget=forms.HiddenInput(), required = False)
    class Meta:
        model = Feedback
        fields = ['text', 'name', 'contact']

