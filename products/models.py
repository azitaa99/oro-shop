from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from accounts.models import MyUser

class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
 


    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'

    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('products:category',args=[self.slug])
    


class Product(models.Model):
    title=models.CharField(max_length=100 ,verbose_name="عنوان محصول")
    info=models.CharField(max_length=1000, verbose_name='توضیحات محصول')
    price=models.IntegerField(verbose_name='قیمت محصول')
    quantity=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(20)] , verbose_name='موجودی ')
    is_active=models.BooleanField(default=True , verbose_name='موجود')
    image=models.ImageField(upload_to='products', blank=True, null=True,verbose_name='تصویر محصول')
    brand=models.CharField(max_length=100,verbose_name='برند محصول')
    posting_detail=models.CharField(max_length=500,verbose_name='جزییات ارسال')
    new_old=models.BooleanField(default=False,verbose_name='جدید/ قدیمی')
    special=models.BooleanField(default=False,verbose_name='محصول ویژه')
    categories=models.ForeignKey(Categories, on_delete=models.CASCADE,related_name='products',verbose_name='دسته بندی')
    view=models.IntegerField(default=0,verbose_name='تعداد بازدید')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
  


    class Meta:
        verbose_name='محصول'
        verbose_name_plural="محصولات"
        ordering=('created',)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('products:products_detail', args=(self.id))
    


class Comment(models.Model):
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ucomments', verbose_name="کاربر")
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pcomments', verbose_name="محصول")
    body=models.TextField(max_length=500 ,verbose_name="متن")
    is_reply=models.BooleanField(default=False)
    reply=models.ForeignKey('Comment',on_delete=models.CASCADE, related_name='rcomment',verbose_name="پاسخ",blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ثبت نظر")

    class Meta:
        verbose_name='نظر کاربران'
        verbose_name_plural='نظرات کاربران'

    def __str__(self) -> str:
        return f'{self.user.email}-{self.body[:30]}'






# Create your models here.
