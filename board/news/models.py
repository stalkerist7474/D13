from asyncio.windows_events import NULL
from email.policy import default
from msilib.schema import Media
from re import I
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from ads.models import User


def post_author_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'file_post_{0}/{1}'.format(instance.id, filename) 

def post_image_author_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'image_post_{0}/{1}'.format(instance.id, filename)


class ImagePost(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to=post_image_author_directory_path, null=True)
    

    def __str__(self):
        return f'{self.title.title()}'

class FilePost(models.Model):
    title = models.CharField(max_length = 255)
    file = models.FileField(upload_to=post_author_directory_path, null=True,validators=[FileExtensionValidator(['mp4'])])
    

    def __str__(self):
        return f'{self.title.title()}'






class Post(models.Model):
    
    post_author = models.ForeignKey(User, on_delete = models.CASCADE)
    post_date_created = models.DateField(auto_now_add = True)
    post_detailed_time_created = models.TimeField(auto_now_add = True)
    head_of_post = models.CharField(max_length = 255)
    article_text = models.TextField()
    post_images = models.ManyToManyField(ImagePost, blank=True)
    post_files = models.ManyToManyField(FilePost, blank=True)

    def __str__(self):
        return f'{self.head_of_post.title()}'

    def get_absolute_url(self): 
        return f'/posts/{self.id}'