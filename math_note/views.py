from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect
from django.views.generic import ListView # new
from django.urls import reverse_lazy # new
from .forms import PostForm # new


def HomePageView(request):
    model = Post.objects.all()
    return render(request, 'math_note/home.html', {'model': model})

def newPage(request):
    if request.method == 'POST':


        book = request.POST['book']
        page = request.POST['page']
        number = request.POST['number']
        WR = request.POST['WR']
        big_unit = choosing_big_unit(book, page)
        middle_unit = choosing_middle_unit(book, page)
        image = request.FILES['image']




        newPost = Post(
            book = book,
            page = page,
            number = number,
            WR = WR,
            big_unit = big_unit,
            middle_unit = middle_unit,
            image = image,
        )
        newPost.save()
        return redirect('detail-page', id=newPost.id)
    else:
        note_form = PostForm

        return render(request, 'math_note/forms.html', {'form': note_form})

def detailPage(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'math_note/detail.html', {'post': post})

# class CreatePostView(CreateView): # new
#     model = Post
#     form_class = PostForm
#     template_name = 'post.html'
#     success_url = reverse_lazy('home')





def choosing_big_unit(book, page):
    page = int(page)
    if book == '개념책' or book == '개념책/예제':
        if page <= 7:
            return '설명'
        elif page <= 31:
            return '소인수분해'
        elif page <= 71:
            return '정수와 유리수'
        elif page <= 117:
            return '문자와 식'
        else:
            return '좌표평면과 그래프'
    else:
        if page <= 39:
            return '소단원 실전 테스트'
        elif page <= 63:
            return '중단원 실전 테스트'
        else:
            return '중단원 서술형 대비'






def choosing_middle_unit(book, page):
    page = int(page)
    if book == '개념책' or book == '개념책/예제':
        if page <= 31 or 117 < page:
            return   choosing_big_unit(book, page)
        else:
            if page <= 49:
                return '정수와 유리수'
            elif page <= 71:
                return '정수와 유리수의 계산'
            elif page <= 97:
                return '문자의 사용과 식의 계산'
            else:
                return '일차방정식'
    else:
        if page < 4:
            return '설명'
        elif page < 10 or (40 <= page and page < 44) or (64 <= page and page < 68):
            return '소인수분해'
        elif page < 18 or (44 <= page or page < 52) or (68<= page or page < 76):
            return '정수와 유리수'
        elif page < 32 or (52 <= page or page < 60) or (76 <= page or page < 84):
            return '문자와 식'
        else:
            return '좌표평면과 그래프'