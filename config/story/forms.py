from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    canvas_image = forms.CharField(widget=forms.HiddenInput)
    plus_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control shadow-none',
            'placeholder': '내용을 입력하세요',
            'aria-label': 'Search...',
            'id' : "textUpload",
            'type': 'text',
        })
    )

    class Meta:
        model = Story
        fields = ('plus_text', )
