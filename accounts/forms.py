from django import forms
from. models import MyUser,OtpCode
from django.core.exceptions import ValidationError



class UserCreatationForm(forms.ModelForm):
    password1=forms.CharField(label='پسورد',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='تکرار پسورد',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model= MyUser
        fields=['full_name', 'email','phone_number']
        widgets={
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'})
        }
    
    def clean_password2(self):
        p1=self.cleaned_data['password1']
        p2=self.cleaned_data['password2']
        if p1 and p2 and p1!=p2:
            raise ValidationError('passwords must be match')
        return p2
    
    def clean_email(self):
        myemail=self.cleaned_data['email']
        user=MyUser.objects.filter(email=myemail).exists()
        if user:
            raise ValidationError('this email exist!')
        return myemail
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user








class loginForm(forms.Form):
    email=forms.EmailField(label='ایمیل',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='پسورد',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class PhoneNumberForm(forms.Form):
    phone_number=forms.IntegerField(label='شماره تلفن',widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean_phone_number(self):
        phone=self.cleaned_data['phone_number']
        user=MyUser.objects.filter(phone_number=phone).exists()
        if user:
            return phone
        else:
            raise ValidationError('شماره تلفن وارد شده در سیستم موجود نمیباشد')
    
class logincodeForm(forms.Form):
    code=forms.IntegerField(label=' کد',widget=forms.TextInput(attrs={'class':'form-control'}))