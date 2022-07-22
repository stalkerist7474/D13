from fileinput import filename
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Ad
from .forms import AdsForm,AdsFormImage,AdsFormFile
from .filters import AdFilter
from django.core.files.storage import FileSystemStorage


# дженерик списка объявлений
class AdsList(ListView):
    model = Ad  
    template_name = 'ads.html'  
    context_object_name = 'ads' 
    paginate_by = 2
    ordering = ['-id']

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = AdFilter(self.request.GET, queryset=self.get_queryset()) 
        

        context['head_of_ad'] = Ad.objects.all()
        context['article_text'] = Ad.objects.all()
        context['ad_author'] = Ad.objects.all()
        context['ad_category'] = Ad.objects.all()
        context['ad_date_created'] = Ad.objects.all()

        context['ad_images'] = Ad.objects.all()
        context['ad_files'] = Ad.objects.all()


        context['form'] = AdsForm()
        context['formImage'] = AdsFormImage()
        
        return context
    
    def post(self, request, *args, **kwargs):
        form = AdsForm(request.POST) 
 
        if form.is_valid(): 
            form.save()
 
        return super().get(request, *args, **kwargs)

# дженерик поиска
class AdListForSearck(ListView):
    model = Ad
    template_name = 'search.html'  
    context_object_name = 'searchAds'
    queryset = Ad.objects.order_by('-id')  
    

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = AdFilter(self.request.GET, queryset=self.get_queryset()) 
        return context

# дженерик для подробной информации
class AdsDetail(DetailView):
    model = Ad 
    template_name = 'adsDetail.html' 
    context_object_name = 'adsDetail' 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['ad_images'] = Ad.objects.all()
        context['ad_files'] = Ad.objects.all()
        return context
    
# дженерик для загрузки картинок
class LoadImageView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'loadImage.html'
    form_class = AdsFormImage
    permission_required = ('ads.add_post',
                           'ads.view_post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

    def post(self, request, *args, **kwargs):
        form = AdsFormImage(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
 
        return super().get(request, *args, **kwargs)

# дженерик для загрузки файлов
class LoadFileView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'loadFile.html'
    form_class = AdsFormFile
    permission_required = ('ads.add_post',
                           'ads.view_post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

    def post(self, request, *args, **kwargs):
        form = AdsFormFile(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
 
        return super().get(request, *args, **kwargs)

# дженерик для создания объекта
class AdsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'create_ads.html'
    form_class = AdsForm
    permission_required = ('ads.add_post',
                           'ads.view_post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

# дженерик для редактирования объекта
class AdsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'ads_update.html'
    form_class = AdsForm
    permission_required = ('ads.change_post',
                           'ads.view_post')
 
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context
 
# дженерик для удаления 
class AdsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'ads_delete.html'
    queryset = Ad.objects.all()
    success_url = '/ads/'
    permission_required = ('ads.delete_post',
                           'ads.view_post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context