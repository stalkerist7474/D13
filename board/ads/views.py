from fileinput import filename
from django.shortcuts import render,redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Ad, Response
from sign.models import MyUser
from .forms import AdsForm,AdsFormImage,AdsFormFile,ResponseForm
from .filters import AdFilter,ResponseFilter

from django.template.loader import render_to_string
from django.http import HttpResponse, HttpRequest
from django.core.mail import EmailMultiAlternatives

# СЕКЦИЯ ОБЪЯВЛЕНИЙ_________________________________________________________________________________
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
        context['ad_author'] = Ad.objects.select_related('ad_author').all()
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
class LoadImageView(LoginRequiredMixin, CreateView):
    template_name = 'loadImage.html'
    form_class = AdsFormImage
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

    def post(self, request, *args, **kwargs):
        form = AdsFormImage(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
 
        return super().get(request, *args, **kwargs)

# дженерик для загрузки файлов
class LoadFileView(LoginRequiredMixin, CreateView):
    template_name = 'loadFile.html'
    form_class = AdsFormFile
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

    def post(self, request, *args, **kwargs):
        form = AdsFormFile(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
 
        return super().get(request, *args, **kwargs)

# дженерик для создания объекта
class AdsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_ads.html'
    form_class = AdsForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

# дженерик для редактирования объекта
class AdsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'ads_update.html'
    form_class = AdsForm
    
 
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context
 
# дженерик для удаления 
class AdsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'ads_delete.html'
    queryset = Ad.objects.all()
    success_url = '/ads/'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

# дженерик списка объявлений одного юзера
class AdsUserView(LoginRequiredMixin, ListView):
    
    model = Ad
    template_name = 'userAdsList.html'
    context_object_name = 'ads'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        user_id = MyUser.objects.get(username=self.request.user).id
        return {
            **super().get_context_data(*args, **kwargs),
            'ads': Ad.objects.filter(user_id=user_id)
        }

# СЕКЦИЯ ОТКЛИКОВ_________________________________________________________________________________
# дженерик списка 
class ResponseList(ListView):
    model = Response
    template_name = 'response/responsesList.html'
    context_object_name = 'responses'
    paginate_by = 3
    

    def get_context_data(self, *args, **kwargs):
        user_id = MyUser.objects.get(username=self.request.user).id
        
        ad_id = Ad.objects.filter(ad_author=user_id)
        
        context = super().get_context_data(*args, **kwargs)
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        context['responses'] = Response.objects.filter(ad_response_id__in=ad_id)
             
        return context
    

# дженерик для подробной информации
class ResponseDetail(DetailView):
    model = Response
    template_name = 'response/responsesDetail.html'
    context_object_name = 'response'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Response.objects.get(pk=id)
    

# дженерик для создания объекта
class ResponseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'response/responsesCreate.html'
    form_class = ResponseForm
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'adsDetail': self.get_object()
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            replies = Response(
                response_text=request.POST['response_text'],
                ad_response_id=self.get_object().id,
                response_user=self.request.user
            )
            replies.save()
        return redirect('/ads/')
    

# дженерик для удаления 
class ResponseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'response/responsesDelete.html'
    queryset = Response.objects.all()
    success_url = '/ads/user_responses/'
    

# функция для принятия отклика 
def Response_accept(request, *args, **kwargs):
    response = Response.objects.get(id=kwargs['pk'])
    user_response_id = response.response_user.id
    user = MyUser.objects.get(id=user_response_id)

    html_content = render_to_string(
        'response/email_response_reply.html',
        {
            'user': user
        }
    )
    msg = EmailMultiAlternatives(
        subject={response.response_text[:20]},
        body=f"Ответ на отклик",
        from_email='TestDjango1@yandex.ru',
        to=[user.email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse('<h1>Готово!</h1>')