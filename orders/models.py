from django.db import models
from accounts.models import MyUser
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator






class Order(models.Model):
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE , related_name='orders',verbose_name='کاربر')
    is_paid=models.BooleanField(default=False, verbose_name='وضعیت پرداخت')
    Created=models.DateTimeField(auto_now=True, verbose_name='تاریج ثبت سفارش')
    discount=models.IntegerField(blank=True, null=True, default=0, verbose_name='درصد تخفیف')
    random_code=models.PositiveIntegerField(blank=True,null=True, unique=True, verbose_name='کد سفارش')
    
 
 
  
    class Meta:
        verbose_name='سبد خرید'
        verbose_name_plural='سفارشات'


    def __str__(self) -> str:
        return f'{self.user.full_name} create order'
    
    
    def get_total_price(self):
        order_cost=sum(item.get_cost() for item in self.items.all() )
        price= (self.discount /100) * order_cost
        return int(order_cost - price)
    
    
    def order_cost(self):
        return sum(item.get_cost() for item in self.items.all() )

        
    
    



class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE , related_name='items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE ,verbose_name='محصول')
    quantity=models.PositiveIntegerField(verbose_name='تعداد')
    price=models.PositiveIntegerField(verbose_name='قیمت')

    class Meta:
        verbose_name='جزییات سبد خرید'
        verbose_name_plural='اطلاعات سبد خرید کاربران'


    def __str__(self) -> str:
        return f'{self.id }'
    
    def get_cost(self):
        return self.quantity *self.price
    
   
            
    
class Senderinfo(models.Model):
  
    full_name = models.CharField(max_length=500, verbose_name="نام ونام خانوادگی")
    phone = models.CharField(max_length=15, verbose_name="تلفن")
    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل")
    address = models.CharField(max_length=1000, verbose_name="آدرس")
    city = models.CharField(max_length=500, verbose_name="شهر")
    postal_code = models.CharField(max_length=25, verbose_name="کد پستی")
    order=models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="سفارش ")



    class Meta:
        verbose_name = "اطلاعات ارسال"
        verbose_name_plural = "اطلاعات ارسال"

    def __str__(self):
        return self.full_name

    


class Coupon(models.Model):
    code=models.CharField(max_length=30, unique=True)
    valid_from=models.DateTimeField()
    valid_to=models.DateTimeField()
    active=models.BooleanField(default=False)
    discount=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)])

    class Meta:
        verbose_name = " کد تخفیف"
        verbose_name_plural = "کدهای تخفیف "


# Create your models here.
