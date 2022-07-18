from pyexpat import model
from django.forms import ModelForm
from .models import Ad, Image, File
from django import forms
 
# Создаём модельную форму
class AdsForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['head_of_ad', 'article_text', 'ad_author', 'ad_category', 'ad_images', 'ad_files']


class AdsFormImage(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']

class AdsFormFile(ModelForm):
    class Meta:
        model = File
        fields = ['title', 'file']