from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request): #blog.urls.py 에서 이 함수를 특정 url 과 연결한다. path('', views.post_list, name='post_list'),
    objs = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':objs})   #'posts':objs  ->  템플릿테그:변수
    # 템플릿을 연결하고 텝플릿 내부의 변수를 정의한다.