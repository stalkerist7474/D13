from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    
    post_author = models.ForeignKey(User, on_delete = models.CASCADE)
    post_date_created = models.DateField(auto_now_add = True)
    post_detailed_time_created = models.TimeField(auto_now_add = True)
    head_of_post = models.CharField(max_length = 255)
    article_text = models.TextField()

    def __str__(self):
        return f'{self.head_of_post.title()}'