from django.shortcuts import render

# Create your views here.
def english_note_home_page(request):
    return render(request, 'english_note/home.html')