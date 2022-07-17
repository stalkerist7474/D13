from django.urls import path
from .views import  PostList, PostDetail, PostListForSearck
from django.views.decorators.cache import cache_page


urlpatterns = [
    
   
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='postDetail'),
    path('search', PostListForSearck.as_view()),
    
]