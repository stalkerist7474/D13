from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm
from .filters import PostFilter




class PostList(ListView):
    model = Post  
    template_name = 'post.html'  
    context_object_name = 'posts' 
    paginate_by = 1


    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) 
        

        context['head_of_post'] = Post.objects.all()
        context['article_text'] = Post.objects.all()
        context['post_author'] = Post.objects.all()
        context['post_date_created'] = Post.objects.all()


        context['form'] = PostForm()
        
        return context
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST) 
 
        if form.is_valid(): 
            form.save()
 
        return super().get(request, *args, **kwargs)



class PostListForSearck(ListView):
    model = Post
    template_name = 'searchPost.html'  
    context_object_name = 'searchPost'
    queryset = Post.objects.order_by('-id')  
    

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) 
        return context









class PostDetail(DetailView):
    model = Post 
    template_name = 'postDetail.html' 
    context_object_name = 'postDetail' 
    #queryset = Post.objects.filter()