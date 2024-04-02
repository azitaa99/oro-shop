from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from.models import MyUser,OtpCode
from django.urls import reverse_lazy,reverse
from .forms import UserCreatationForm, loginForm,PhoneNumberForm,logincodeForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views import View
from django.contrib.auth import logout,login, authenticate
import random
from utils import otpcode_sender
import datetime
from django.utils import timezone




class UserRegister(FormView):
    form_class=UserCreatationForm
    template_name='accounts/register.html'
    success_url=reverse_lazy('home:home')

    def form_valid(self, form):
        self._create_user(form.cleaned_data)
        messages.success(self.request,'you register successfully', 'success')
        return super().form_valid(form)
    
    def _create_user(self,data):
        MyUser.objects.create_user(full_name=data['full_name'],
                            email=data['email'],
                            phone_number=data['phone_number'],
                            password=data['password2'] )

class Userlogin(View):
    form_class= loginForm
    def get(self, request,code_id=None):
        if code_id:
             return render(request,'accounts/logincode.html',{'form':logincodeForm})
        form=self.form_class
        return render(request,'accounts/login.html',{'form':form})
    
    def post(self, request,code_id=None):

        if code_id:
            form= logincodeForm(request.POST)
            user_session=request.session['userlogininfo']
            now= timezone.now()
            delta=datetime.timedelta(minutes=1 )
            if form.is_valid():
                code_instance=OtpCode.objects.filter(phone_number=user_session['phone_number']).last()
                code=form.cleaned_data['code']
                if code == code_instance.code:
                    if now > code_instance.created + delta:
                        messages.error(request,'کد منقضی شده دوباره درخواست کنید','danger')
                        return redirect('accounts:login_sms')
                    else:
                        user=MyUser.objects.get(phone_number=user_session['phone_number'])
                        login(request,user)
                        code_instance.delete()
                        messages.success(request,'your enter successfully', 'info')
                        return redirect('home:home')
                else:
                   messages.error(request,'کد وارد شده اشتباه است','danger')
                   return redirect('accounts:login_with_code', code_instance.id)
            
            return redirect('accounts:login_sms')   
            

        form =self.form_class(request.POST)
        if form.is_valid():
            user=authenticate(request,email=form.cleaned_data['email'],password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'your enter successfully', 'info')
                return redirect('home:home')
            messages.error(request,'ایمیل یا پسورد اشتباه است','danger')
        return render(request,'accounts/login.html',{'form':form})
            
    
class UserLoginCode(View):
    form_class=PhoneNumberForm
    def get(self, request):
        
        return render(request,'accounts/loginsms.html',{'form':self.form_class})
    def post(self,request):
        
        form=self.form_class(request.POST)
        if form.is_valid():
            request.session['userlogininfo']={'phone_number':form.cleaned_data['phone_number']}
            code=random.randint(999,9999)
            otpcode_sender(form.cleaned_data['phone_number'],code)
            mycode=OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'],code=code)
           
            return redirect('accounts:login_with_code', mycode.id)
        messages.error(request,'شماره تلفن وارد شده در سیستم موجود نمیباشد','danger')
        return render(request,'accounts/loginsms.html',{'form':self.form_class})
    

        

    


class Userlogout(View):
    def get(self,request):
        logout(request)
        messages.success(request,'you logout successfully','success')
        return redirect('home:home')
    




# connecting google 
    
class userpasswordresetView(auth_views.PasswordResetView):
    template_name='accounts/pass_reset_form.html'
    success_url=reverse_lazy('accounts:pass_reset_done')
    email_template_name='accounts/pass_reset_email.html'


class userpasswordresetdoneview(auth_views.PasswordResetDoneView):
    template_name='accounts/pass_reset_done.html'


class userpasswordresetconfirmview(auth_views.PasswordResetConfirmView):
    template_name='accounts/pass_reset_confirm.html'
    success_url=reverse_lazy('accounts:pass_reset_complete')


class userpasswordresetcompleteview(auth_views.PasswordResetCompleteView):
    template_name='accounts/pass_reset_complete.html'



            








