from pyexpat import model
from django.forms import ModelForm
from .models import Post
from django import forms
 
# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['head_of_post', 'article_text', 'post_images', 'post_files']


