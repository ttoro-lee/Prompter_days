from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
    character_name = forms.CharField(
        label="친구의 이름",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
    )
    age = forms.ChoiceField(
        label="나이",
        widget=forms.Select(attrs={"class": "form-select form-select-lg"}),
        choices=[(str(i), str(i)) for i in range(5, 11)],
    )
    gender = forms.ChoiceField(
        label="성별",
        widget=forms.Select(attrs={"class": "form-select form-select-lg"}),
        choices=[("male", "남"), ("female", "여")],
    )
    likes = forms.CharField(
        label="좋아하는 것",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
    )
    dislikes = forms.CharField(
        label="싫어하는 것",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
    )

    class Meta:
        model = Friend
        fields = ('character_name', 'age', 'gender', 'likes', 'dislikes')
