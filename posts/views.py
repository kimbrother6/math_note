# posts/views.py
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .forms import PostForm # new


def HomePageView(request):
    model = Post.objects.all()
    return render(request, 'posts/home.html', {'model': model})

def newPage(request):
    if request.method == 'POST':
        
        newPost = Post(
            book = request.POST['book'],
            page = request.POST['page'],
            number = request.POST['number'],
            WR = request.POST['WR'],
            image = request.FILES['image'],
        )
        newPost.save()
        return redirect('detail-page', id=newPost.id)
    else:
        note_form = PostForm
        return render(request, 'posts/forms.html', {'form': note_form})

def detailPage(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'posts/detail.html', {'post': post})

# class CreatePostView(CreateView): # new
#     model = Post
#     form_class = PostForm
#     template_name = 'post.html'
#     success_url = reverse_lazy('home')
