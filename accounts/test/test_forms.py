from django.test import TestCase
from accounts.forms import UserCreatationForm,logincodeForm
from accounts.models import MyUser



class testUserCreatationForm(TestCase):

    
    
    def test_valid_data(self):
        form = UserCreatationForm(data = {
            'full_name' :'azita tahbaz',
            'email' :'azita@email.com',
            'phone_number' : '09126199127',
            'password1':'123456',
            'password2':'123456'
        })
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        form=UserCreatationForm(data={})
        self.assertEqual(len(form.errors),5)
        self.assertFalse(form.is_valid())

    def test_clean_password2(self):
        form=UserCreatationForm(data= {
            'full_name' :'azita tahbaz',
            'email' :'azita@email.com',
            'phone_number' : '09126199127',
            'password1':'123456',
            'password2':'1234567'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)
    
    def test_clean_email(self):
        MyUser.objects.create(
            full_name='jack',
            email='jack@email.com',
            phone_number='09121231234',
            city='tehran',
            age='23'
        )
        form=UserCreatationForm(data= {
            'full_name' :'azita',
            'email' :'jack@email.com',
            'phone_number' : '09126199127',
            'password1':'123456',
            'password2':'123456'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)
        self.assertTrue(form.has_error('email'))

class testUserCloginForm(TestCase):

    def test_login_code_invalid_form(self):
        form=logincodeForm(data={'code':'abcs'})
        self.assertEqual(len(form.errors),1)
        self.assertTrue(form.has_error('code'))