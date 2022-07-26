from asyncio.windows_events import NULL
from email.policy import default
from msilib.schema import Media
from re import I
from django.db import models
from django.contrib.auth.models import User
from sign.models import User


from django.core.validators import FileExtensionValidator



def ad_author_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'file_{0}/{1}'.format(instance.id, filename) 

def ad_image_author_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'image_{0}/{1}'.format(instance.id, filename)


class Image(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to=ad_image_author_directory_path, null=True)
    #author = models.OneToOneField(User, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title.title()}'

class File(models.Model):
    title = models.CharField(max_length = 255)
    file = models.FileField(upload_to=ad_author_directory_path, null=True,validators=[FileExtensionValidator(['mp4'])])
    #author = models.OneToOneField(User, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title.title()}'


class Ad(models.Model):
    tank = 'TK'
    heal = 'HL'
    damage_dealer = 'DD'
    trader = 'TR'
    guildmaster = 'GM'
    quest_giver = 'QG'
    blacksmith = 'BS'
    tanners = 'TN'
    potion_makers = 'PM'
    spell_masters = 'SM'
    


    ROLE=[
    (tank,'Танки'),
    (heal,'Хилы'),
    (damage_dealer,'ДД'),
    (trader,'Торговцы'),
    (guildmaster,'Гилдмастеры'),
    (quest_giver,'Квестгиверы'),
    (blacksmith,'Кузнецы'), 
    (tanners,'Кожевники'),
    (potion_makers,'Зельевары'),
    (spell_masters,'Мастера заклинаний')]

    
    head_of_ad = models.CharField(max_length = 255)
    article_text = models.TextField() 
    ad_author = models.ForeignKey(User, on_delete = models.CASCADE)
    ad_date_created = models.DateField(auto_now_add = True)
    ad_detailed_time_created = models.TimeField(auto_now_add = True)
    ad_category = models.CharField(max_length=2, choices= ROLE)
    ad_images = models.ManyToManyField(Image, blank=True)
    ad_files = models.ManyToManyField(File, blank=True)

    def __str__(self):
        return f'{self.head_of_ad.title()}'

    def get_absolute_url(self): 
        return f'/ads/{self.id}'




class Response(models.Model):
    ad = models.ForeignKey(Ad, on_delete = models.CASCADE)
    response_user = models.ForeignKey(User,on_delete = models.CASCADE)
    response_text = models.TextField()
    


    
    


