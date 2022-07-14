from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post




class PostList(ListView):
    model = Post  
    template_name = 'post.html'  
    context_object_name = 'posts' 
    paginate_by = 1


class PostDetail(DetailView):
    model = Post 
    template_name = 'postDetail.html' 
    context_object_name = 'postDetail' 
    #queryset = Post.objects.filter()