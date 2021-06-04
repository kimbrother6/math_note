from django.shortcuts import render, redirect
from .models import Sentence
from .forms import englishNoteForm
from sqlalchemy import create_engine
import pandas as pd


engine = create_engine("sqlite:////Users/cubest_june/hj-django/note/db.sqlite3")


# Create your views here.
def english_note_home_page(request):
    sentenc = Sentence.objects.all()

    with engine.connect() as conn, conn.begin():
            data = pd.read_sql_table("english_note_sentence", conn)
    Classification_list = data['Classification'].unique()
    
    context = {
        'sentenc': sentenc,
        'Classification_list': Classification_list
    }
    print(context)
    return render(request, 'english_note/home.html', context=context)


def sentenceCard(request, listName, listId):
    sentence = Sentence.objects.filter(Classification=listName)
    return render(request, 'english_note/sentenceCard.html', {'sentences':sentence, 'listId': listId})



# def blind_detail_page(request):
#     sentenc = Sentence.objects.all()

#     with engine.connect() as conn, conn.begin():
#             data = pd.read_sql_table("english_note_sentence", conn)
#     Classification_list = data['Classification'].unique()
    
#     context = {
#         'sentenc': sentenc,
#         'Classification_list': Classification_list
#     }
#     print(context)

#     return render(request, 'english_note/blind_detail.html', context=context)

# def open_detail_page(request, id):
#     sentence = Sentence.objects.get(id=id)
#     return render(request, 'english_note/open_detail.html', {'sentenc': sentence})




def new_page(request):
    if request.method == 'POST':

        Memorization = request.POST['Memorization']
        Classification = request.POST['Classification']

        

        new_sentence = Sentence(
            english_sentence = request.POST['english_sentence'],
            korean_sentence = request.POST['korean_sentence'],
            Memorization = Memorization,
            Classification = Classification,
        )
        new_sentence.save()
        return redirect('/english_note/')
    else:
        form = englishNoteForm
        return render(request, 'english_note/forms.html', {'form': form})