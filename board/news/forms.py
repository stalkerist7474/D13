from pyexpat import model
from django.forms import ModelForm
from .models import Post, ImagePost, FilePost

 
# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['head_of_post', 'article_text', 'post_author','post_images', 'post_files']


class PostFormImage(ModelForm):
    class Meta:
        model = ImagePost
        fields = ['title',  'image']

class PostFormFile(ModelForm):
    class Meta:
        model = FilePost
        fields = ['title',  'file']