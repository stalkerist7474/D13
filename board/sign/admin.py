
from django.contrib import admin
from .models import MyUser




class MyUserAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('username', 'full_name', 'email', 'is_active','is_staff', ) # оставляем только имя и цену товара
    list_filter = ('gender', 'is_active', ) # добавляем примитивные фильтры в нашу админку
    






admin.site.register(MyUser,MyUserAdmin)