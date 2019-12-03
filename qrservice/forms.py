from django import forms

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"autofocus": "", "placeholder": "Опиши свой визит к нам"}))

    class Meta:
        model = Feedback
        fields = ['text', 'name', 'contact']

