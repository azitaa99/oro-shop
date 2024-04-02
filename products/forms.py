from django.forms import forms , ModelForm
from .models import Comment,Product
from django import forms

class commentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['body',]
        widgets={
        'body':forms.Textarea(attrs={'cols':140,'rows':5})
        }
        labels={
            'body':'متن نظر'
        }


class replyForm(ModelForm):
    class Meta:
        model=Comment
        fields=['body',]

class addform(forms.Form):
    quantity=forms.IntegerField(min_value=1)
   


