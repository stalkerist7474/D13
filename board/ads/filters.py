from django_filters import FilterSet
 
from .models import Ad
 
 
# создаём фильтр
class AdFilter(FilterSet):
    
    class Meta:
        model = Ad
        fields = {
            'head_of_ad': ['icontains'], 
            'ad_date_created': ['gt'],
            'ad_category': ['icontains'], 
            'ad_author': ['in'], 
        }