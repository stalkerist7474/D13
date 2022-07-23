from django.urls import path
from .views import  PostList, PostDetail, PostListForSearck,LoadImageView,LoadFileView, PostCreateView,PostUpdateView,PostDeleteView
from django.views.decorators.cache import cache_page


urlpatterns = [
    
   
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='postDetail'),
    path('search', PostListForSearck.as_view()),

    path('add/', PostCreateView.as_view(), name='create_posts'), 
    path('edit/<int:pk>', PostUpdateView.as_view(), name='posts_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='posts_delete'),

    path('loadImages/', LoadImageView.as_view(), name='loadImage'),
    path('loadFiles/', LoadFileView.as_view(), name='loadFile'),
    
]