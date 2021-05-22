from django.urls import path
from . import views
# from .views import CreatePostView

urlpatterns = [
    path('posts/', views.HomePageView, name='home-page'),
    path('posts/new', views.newPage, name='new-page'),
    path('posts/<int:id>/', views.detailPage, name='detail-page')
]