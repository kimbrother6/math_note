from django.shortcuts import render, redirect
from .models import Sentence
from .forms import englishNoteForm

# Create your views here.
def english_note_home_page(request):
    return render(request, 'english_note/home.html')

def blind_detail_page(request):
    sentenc = Sentence.objects.all()
    return render(request, 'english_note/blind_detail.html', {'sentenc': sentenc})

def open_detail_page(request, id):
    sentence = Sentence.objects.get(id=id)
    return render(request, 'english_note/open_detail.html', {'sentenc': sentence})

def new_page(request):
    if request.method == 'POST':
        new_sentence = Sentence(
            english_sentence = request.POST['english_sentence'],
            korean_sentence = request.POST['korean_sentence'],
            Memorization = request.POST['Memorization'],
            Classification = request.POST['Classification'],
        )
        new_sentence.save()
        return redirect('/english_note/blind/')
    else:
        form = englishNoteForm
        return render(request, 'english_note/forms.html', {'form': form})