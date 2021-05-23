from django.urls import path
from . import views
# from .views import CreatePostView

urlpatterns = [
    path('', views.english_note_home_page, name='list-page'),
]