from django.conf import settings # new
from django.urls import path, include # new
from . import views

urlpatterns = [
    path('math_note/', include('math_note.urls'), name='math-note'),
    path('', views.home_page)
]