from django.db.models import fields
from django.forms import ModelForm
from .models import Submisyon, Digitaltype

class SubmisyonForm(ModelForm):
    class Meta:
        model = Submisyon
        fields = ['fnam', 'emayl', 'seks', 'countri', 'descr']

class DigitalForm(ModelForm):
    class Meta:
        model = Digitaltype
        fields = ['tda', 'reso', 'orient', 'nameart', 'prays', 'curr']
 
