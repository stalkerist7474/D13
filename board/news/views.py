from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
from .forms import PostForm,PostFormFile,PostFormImage
from .filters import PostFilter


class PostList(ListView):
    model = Post  
    template_name = 'post.html'  
    context_object_name = 'posts' 
    paginate_by = 3

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



# дженерик для загрузки картинок
class LoadImageView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'loadImage.html'
    form_class = PostFormImage
    permission_required = ('posts.add_post',
                           'posts.view_post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

    def post(self, request, *args, **kwargs):
        form = PostFormImage(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
 
        return super().get(request, *args, **kwargs)

# дженерик для загрузки файлов
class LoadFileView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'loadFile.html'
    form_class = PostFormFile
    permission_required = ('posts.add_post',
                           'posts.view_post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

    def post(self, request, *args, **kwargs):
        form = PostFormFile(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
 
        return super().get(request, *args, **kwargs)

# дженерик для создания объекта
class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'create_posts.html'
    form_class = PostForm
    permission_required = ('posts.add_post',
                           'posts.view_post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

# дженерик для редактирования объекта
class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'posts_update.html'
    form_class = PostForm
    permission_required = ('posts.change_post',
                           'posts.view_post')
    context_object_name = 'posts'
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context
 
# дженерик для удаления 
class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'posts_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'
    permission_required = ('posts.delete_post',
                           'posts.view_post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context