from django.forms import ModelForm
from .models import New, Zone, Category


class NewForm(ModelForm):
    class Meta:
        model = New
        fields = ['title', 'description', 'body', 'image', 'is_active', 'zone', 'category', 'hashtags']


class ZoneForm(ModelForm):
    class Meta:
        model = Zone
        fields = ['name', 'slug']



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']