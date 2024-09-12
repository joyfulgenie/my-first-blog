from django.urls import path
from . import views
urlpatterns = [
    # 리스트 목록 페이지
    path('', views.post_list, name='post_list'),
    # 상세 페이지 URL이 http://127.0.0.1:8000/post/1/가 되게 만들것
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 새로 작성 (추가) 메뉴
    path('post/new/', views.post_new, name='post_new'),
    # 편집
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # 미등록글 리스트
    path('post/draft/', views.post_draft_list, name='post_draft_list'),
    #url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    # 등록 출판
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    # 삭제
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    # comment 달기
    path('post/<int:pk>/comment/', views.add_comment_to_post, name = 'add_comment_to_post'),
    # 코멘트 허가
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    # 코멘트 삭제
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]