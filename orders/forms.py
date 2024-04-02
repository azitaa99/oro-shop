from django import forms
from .models import Senderinfo


class senderForm(forms.ModelForm):
    class Meta:
        model=Senderinfo
        exclude=['order']
        


class couponForm(forms.Form):
    code=forms.CharField(max_length=30)
    
    
