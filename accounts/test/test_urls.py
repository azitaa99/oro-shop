from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import UserRegister,Userlogin



class TestUrls(SimpleTestCase):
    def test_register(self):
        url=reverse('accounts:register')
        self.assertEqual(resolve(url).func.view_class, UserRegister)

    def test_login(self):
        url=reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class,Userlogin)