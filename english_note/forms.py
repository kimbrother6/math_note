from django import forms


class englishNoteForm(forms.Form):
    english_sentence = forms.CharField(max_length=200, label='영어 문장')
    korean_sentence = forms.CharField(max_length=200, label='한국어 만장')
    Memorization = forms.ChoiceField(label='외운 정도', choices = [('시작', '시작'), ('어.. 모르겠어', '어.. 모르겠어'), ('어.. 아!', '어.. 아!'), ('이제 알거 같아', '이제 알거 같아'), ('이제 알아', '이제 알아'), ('완벽해!', '완벽해!')])
    Classification = forms.ChoiceField(label='분류', choices=[('영어A 수행평가', '영어A 수행평가')])