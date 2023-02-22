from django.forms import ModelForm
from .models import Tasks

class Task_maker(ModelForm): 
    class Meta: 
        model= Tasks
        fields= ['title','description','important']
