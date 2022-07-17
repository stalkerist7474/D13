from pyexpat import model
from django.forms import ModelForm
from .models import Ad
from django import forms
 
# Создаём модельную форму
class AdsForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['head_of_ad', 'article_text', 'ad_category', 'ad_images', 'ad_files']


