from django.contrib.auth.forms import UserCreationForm
from django import forms


from .models import MyUser


class BaseRegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ["username",
                  "full_name",
                  "email",
                  
                  "gender",
                  "mailing",
                  ]


class VerifiedCodeForm(forms.Form):
    verified_fieid = forms.CharField()