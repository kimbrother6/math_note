from django.conf import settings # new
from django.urls import path, include # new
from . import views

urlpatterns = [
    path('math_note/', include('math_note.urls')),
    path('english_note/', include('english_note.urls')),
    path('', views.home_page)
]