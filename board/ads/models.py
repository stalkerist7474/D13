from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    full_name = models.CharField(max_length = 255)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    #alluath основа
    def __str__(self):
        return f'{self.full_name.title()}'

    

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

    def __str__(self):
        return f'{self.head_of_ad.title()}'
    


class Response(models.Model):
    ad = models.ForeignKey(Ad, on_delete = models.CASCADE)
    response_user = models.ForeignKey(User,on_delete = models.CASCADE)
    response_text = models.TextField()
    


    
    


