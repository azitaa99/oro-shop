from django.test import TestCase,Client,RequestFactory,override_settings
from django.urls import reverse
from accounts.forms import UserCreatationForm,logincodeForm
from accounts.models import MyUser,OtpCode
from model_bakery import baker
from accounts.views import Userlogin
from django.contrib import messages
from unittest import mock
import datetime



class testuserregister(TestCase):


    def setUp(self):
        self.client=Client()
        self.factory=RequestFactory()
        
       

      
       
    def test_user_register_GET(self):
        response=self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'accounts/register.html')
        self.failUnless(response.context['form'],UserCreatationForm)

    def test_user_register_POST_valid(self):
        response=self.client.post(reverse('accounts:register'), data={
            'full_name':'azitaa',
            'email':'azitaa@gmail.com',
            'phone_number':'09114567895',
            'password1':'123456',
            'password2':'123456'
        })
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('home:home'))
        self.assertEqual(MyUser.objects.count(),1)

    def test_user_register_POST_invalid(self):
         response=self.client.post(reverse('accounts:register'), data={
            'full_name':'azitaa',
            'email':'azitaaf',
            'phone_number':'09114567895',
            'password1':'123456',
            'password2':'123456'
        })
         self.assertEqual(response.status_code,200)
         self.failIf(response.context['form'].is_valid())
    


class test_user_login_view_without_code(TestCase):
    def setUp(self):
        self.client=Client()
        user=MyUser.objects.create_user(
            email='usertest@email.com',
            full_name='usertest',
            phone_number='09121111111',
            password='userpass'
        )
        otpcode=OtpCode.objects.create(phone_number='09121234567',code='1234',created=datetime.datetime(2024,1,1,8,0,0))

    def test_user_login_view_without_code(self):
        respone=self.client.post(reverse('accounts:login'),data={
            'email':'usertest@email.com',
            'password':'userpass'
        })
        self.assertEqual(respone.status_code,302)
        self.assertRedirects(respone,reverse('home:home'))

    
    # @override_settings(USE_TZ=False)
    # @mock.patch('accounts.views.Userlogin.now')
    # def test_login_code_valid_form(self,mock_now):
    #      mock_now.side_effect=[
    #          datetime.datetime(2024,1,1,8,2,5)
    #      ]
          
    #      form=logincodeForm(data={'code':'1234'})
    #      OtpCode.objects.create(ohone_number='09121111111',code='1234',created=datetime.datetime(2024,1,1,8,2,0))
    #      session = self.client.session
    #      session['phone_number'] = '09121111111'
    #      session.save()
        
    #      respone=self.client.post(reverse('accounts:login_with_code',{'code_id':'1'}))
    #      self.assertRedirects(respone,reverse('accounts:login_sms'))

        





         
        
        
