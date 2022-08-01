from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):

    MAX_NAME_LENGTH = 100

    man = "MN"
    woman = "WN"
    GENDER = [
        (man, "Мужчина"),
        (woman, "Женщина")
    ]

    id = models.AutoField(auto_created=True, primary_key=True, verbose_name="ID")
    username = models.CharField(max_length=200, blank=False, unique=True)
    email = models.EmailField(blank=False, db_index=True)
    full_name = models.CharField(max_length=MAX_NAME_LENGTH)
    gender = models.CharField(max_length=2, choices=GENDER, default=man)
    mailing = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.username}"


class OneTimeCode(models.Model):
    user = models.OneToOneField(MyUser, null=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)