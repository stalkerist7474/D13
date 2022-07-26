
from django.views.generic.edit import CreateView
from .forms import BaseRegisterForm
from .models import MyUser


class BaseRegisterView(CreateView):
    model = MyUser
    form_class = BaseRegisterForm
    success_url = '/ads/'
