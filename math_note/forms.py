from django import forms


class PostForm(forms.Form):
    book = forms.ChoiceField(choices = [('개념책', '개념책'), ('개념책/예제', '개념책/예제'), ('실전책','실전책')])
    page = forms.IntegerField(max_value=150, min_value=1)
    number = forms.IntegerField(max_value=50, min_value=1)
    WR = forms.CharField(widget=forms.Textarea, label='틀린 이유')
    image = forms.ImageField(label='틀린문제 사진')