from django import forms


class englishNoteForm(forms.Form):
    english_sentence = forms.CharField(max_length=200)
    korean_sentence = forms.CharField(max_length=200)
    Memorization = forms.ChoiceField(choices = [('0', '시작'), ('1', '어.. 모르겠어'), ('2', '어.. 아!'), ('3', '이제 알거 같아'), ('4', '이제 알아'), ('5', '완벽해!')])
    Classification = forms.ChoiceField(choices=[('0', '영어A 수행평가'), ('1', '1'), ('2', '2'), ('3', '3')])