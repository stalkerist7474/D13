from django.urls import path
from .views import AdsList, AdsDetail
from django.views.decorators.cache import cache_page


urlpatterns = [
    
    path('', AdsList.as_view()),
    path('<int:pk>', AdsDetail.as_view(), name='adsDetail'), 
    
]