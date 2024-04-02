from django.contrib import admin
from .models import Senderinfo,Order,OrderItem,Coupon
from django.contrib.auth.admin import UserAdmin


admin.site.register(Coupon)

class orderiteminline(admin.TabularInline):
    model=OrderItem
    can_delete=False

class Senderinfoinline(admin.TabularInline):
    model=Senderinfo
    can_delete=False

@admin.register(Order)
class orderadmin(admin.ModelAdmin):
    inlines=[orderiteminline , Senderinfoinline]

