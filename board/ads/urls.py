from django.urls import path
from .views import AdsList, AdsDetail, AdListForSearck, AdsCreateView, AdsDeleteView, AdsUpdateView
from django.views.decorators.cache import cache_page


urlpatterns = [
    
    path('', AdsList.as_view()),
    path('<int:pk>', AdsDetail.as_view(), name='adsDetail'), 
    path('search', AdListForSearck.as_view()),

    path('add/', AdsCreateView.as_view(), name='create_ads'), 
    path('edit/<int:pk>', AdsUpdateView.as_view(), name='ads_update'),
    path('delete/<int:pk>', AdsDeleteView.as_view(), name='ads_delete'),

]