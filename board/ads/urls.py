from django.urls import path
from .views import AdsList, AdsDetail, AdListForSearck, AdsCreateView, AdsDeleteView, AdsUpdateView,LoadImageView, LoadFileView
from .views import ResponseList, ResponseDetail, ResponseCreateView, ResponseDeleteView, Response_accept, AdsUserView
from django.views.decorators.cache import cache_page


urlpatterns = [
    
    path('', AdsList.as_view()),
    path('<int:pk>', AdsDetail.as_view(), name='adsDetail'), 
    path('search', AdListForSearck.as_view()),

    path('add/', AdsCreateView.as_view(), name='create_ads'), 
    path('edit/<int:pk>', AdsUpdateView.as_view(), name='ads_update'),
    path('delete/<int:pk>', AdsDeleteView.as_view(), name='ads_delete'),

    path('loadImages/', LoadImageView.as_view(), name='loadImage'),
    path('loadFiles/', LoadFileView.as_view(), name='loadFile'),



    path('user_ads/', AdsUserView.as_view(), name='ads_user'),
    path('user_response/', ResponseList.as_view(), name='response_user'),
    path('user_response/<int:pk>/', ResponseDetail.as_view(), name='response_user_detail'),
    path('user_response/<int:pk>/accept/', Response_accept, name='response_accept'),
    path('user_response/<int:pk>/delete/', ResponseDeleteView.as_view(), name='response_delete'),
    path('<int:pk>/create_response/', ResponseCreateView.as_view(), name='response_ad'),

]