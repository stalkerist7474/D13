from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ad




class AdsList(ListView):
    model = Ad  
    template_name = 'ads.html'  
    context_object_name = 'ads' 
    paginate_by = 1


class AdsDetail(DetailView):
    model = Ad 
    template_name = 'adsDetail.html' 
    context_object_name = 'adsDetail' 
    #queryset = Post.objects.filter()