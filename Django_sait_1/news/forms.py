from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            "title": TextInput(attrs={'class':'form-control','placeholder':'Название'})
        ,
            "anons": TextInput(attrs={'class':'form-control','placeholder':'Анонс'})
        ,
            "date": DateTimeInput(attrs={'class':'form-control','placeholder':'Дата публикации'})
        ,
            "full_text": Textarea(attrs={'class':'form-control','placeholder':'Текст'})
        }