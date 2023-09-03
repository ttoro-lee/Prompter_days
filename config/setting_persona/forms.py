from django import forms
from .models import Friend, User

class FriendForm(forms.ModelForm):
    canvas_image = forms.CharField(widget=forms.HiddenInput, label="친구 이미지")
    character_name = forms.CharField(
        label="친구의 이름",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        required=True
    )
    age = forms.ChoiceField(
        label="친구의 나이",
        widget=forms.Select(attrs={"class": "form-select form-select-lg"}),
        choices=[(str(i), str(i)) for i in range(5, 11)],
    )
    gender = forms.ChoiceField(
        label="친구의 성별",
        widget=forms.Select(attrs={"class": "form-select form-select-lg"}),
        choices=[("male", "남"), ("female", "여")],
    )
    likes = forms.CharField(
        label="친구가 좋아하는 것",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        required=True
    )
    dislikes = forms.CharField(
        label="친구가 싫어하는 것",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        required=True
    )

    class Meta:
        model = Friend
        fields = ('character_name', 'age', 'gender', 'likes', 'dislikes')
        
class UserForm(forms.ModelForm):

    user_name = forms.CharField(
        label="나의 이름",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        required=True
    )
    user_age = forms.ChoiceField(
        label="나의 나이",
        widget=forms.Select(attrs={"class": "form-select form-select-lg"}),
        choices=[(str(i), str(i)) for i in range(5, 11)],
    )
    user_gender = forms.ChoiceField(
        label="나의 성별",
        widget=forms.Select(attrs={"class": "form-select form-select-lg"}),
        choices=[("male", "남"), ("female", "여")],
    )

    class Meta:
        model = User
        fields = ('user_name', 'user_age', 'user_gender',)
