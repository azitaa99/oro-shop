from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from.managers import MyUserManager
from django.core.exceptions import ValidationError


class MyUser(AbstractBaseUser,PermissionsMixin):
    full_name=models.CharField(max_length=100,verbose_name='نام و نام خانوادگی')
    email=models.EmailField(unique=True, verbose_name='ایمیل')
    phone_number=models.IntegerField(unique=True,verbose_name='شماره تلفن همراه')
    city=models.CharField(max_length=100,null=True, blank=True,verbose_name='شهر')
    age=models.PositiveSmallIntegerField(null=True, blank=True,verbose_name='سن')
    is_active=models.BooleanField(default=True,verbose_name='فعال')
    is_admin=models.BooleanField(default=False,verbose_name='ادمین')
    created=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ عضویت')
    #manager
    objects = MyUserManager()
    class Meta:
        verbose_name = " کاربر"
        verbose_name_plural = " کاربران"

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name','phone_number']

    def __str__(self):
        return f'{self.email} cerate account at {self.created}'
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




class OtpCode(models.Model):
    phone_number=models.CharField(max_length=12)
    code=models.IntegerField()
    created=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='کد پیامکی'
        verbose_name_plural='کد های پیامکی'

    

    
    
    def __str__(self) -> str:
        return f'{self.phone_number}--{self.code}--{self.created}'

