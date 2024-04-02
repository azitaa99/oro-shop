from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect,get_list_or_404
from django.views import View
from products.models import Product
from .Cart import CART
from products.forms import addform
from .models import Order, OrderItem,Senderinfo,Coupon
from .forms import senderForm, couponForm
from django.views.generic import FormView
from django.urls import reverse_lazy
import random
import datetime
from django.contrib import messages
from  django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages




class CartView(LoginRequiredMixin,View):
    template_name='orders/cartview.html'
    
    def get(self, request):
        cart=CART(request)
        return render(request,self.template_name,{'cart':cart} )


class CartAddView(View):
    def post(self, request,product_id):
        product=get_object_or_404(Product,id=product_id)
        form=addform(request.POST)
        if form.is_valid():
            if form.cleaned_data['quantity'] > product.quantity :
                message = ('بیشترین تعداد قابل سفارش: %(product.quantity)s  عدد میباشد') % {'product.quantity': product.quantity}
                
                messages.error(request, message,'danger')
                return redirect('products:products_detail', product.id )
            card=CART(request)  
            card.add(product,quantity=form.cleaned_data['quantity'])
        return redirect('orders:cart_view')


class RemoveCartView(LoginRequiredMixin,View):
    def get(self,request,product_id):
        product=get_object_or_404(Product,id=product_id)
        cart=CART(request)
        cart.remove(product)
        return redirect('orders:cart_view')
    


class CreateOrderView(LoginRequiredMixin,View):
    def get(self, request):
        code=random.randint(10000,99999)

        cart=CART(request)
        order=Order.objects.create(user=request.user,random_code=code)
        for item in cart:
            OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
        cart.clear()    
        return redirect('orders:detail_order' , order.id)


class DetailOrderView(LoginRequiredMixin,View):
    def get(self, request, order_id):
        form=couponForm
        order=get_object_or_404(Order,id=order_id)

        return render(request, 'orders/detailorder.html', {'order':order, 'form':form})
    
class SenderinfoView(LoginRequiredMixin,FormView):
    form_class=senderForm
    template_name='orders/senderdetail.html'



    def get_success_url(self):
        return reverse_lazy('orders:order_final', kwargs={'order_id': self.get_context_data()['order'].id})

    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        order=Order.objects.get(id=self.kwargs['order_id'])
        context['order']=order
        return context

    def _create_sender(self,data):
        Senderinfo.objects.create(
            full_name=data['full_name'],
            phone=data['phone'],
            email=data['email'],
            address=data['address'],
            city=data['city'],
            postal_code=data['postal_code']
        )


    def form_valid(self, form):
        self._create_sender(form.cleaned_data)
        form.save()
        order=Order.objects.get(id=self.kwargs['order_id'])
       
        return super().form_valid(form)
    
    



class ApplycouponView(LoginRequiredMixin,View):
    form_class=couponForm
    
    def post(self, request,order_id):
        now=datetime.datetime.now()
        form=self.form_class(request.POST)
        if form.is_valid():
            code= form.cleaned_data['code']
            try:
                coupon=Coupon.objects.get(
                    code__exact=code,
                    valid_from__lte=now,
                    valid_to__gte=now
                )
            except Coupon.DoesNotExist:
                messages.error(request,'کد تخفیف نامعتبر است', 'danger')
                return redirect('orders:detail_order', order_id)
            order=Order.objects.get(id=order_id)
            order.discount=coupon.discount
            order.save()
            messages.success(request,'کد تخفیف  اعمال شد', 'success')
           
            return redirect('orders:detail_order' , order.id)



class OrderfinalView(LoginRequiredMixin,View):
    def post(self, request, order_id):
        myorder=Order.objects.get(id=order_id)
        form=senderForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Senderinfo.objects.create(
                order=myorder,
                full_name=cd['full_name'],
                phone = cd['phone'],
                email = cd['email'],
                address = cd['address'],
                city =cd['city'],
                postal_code = cd['postal_code']
            )
            
            for item in myorder.items.all():
                item.product.quantity=item.product.quantity - item.quantity
                if item.product.quantity <= 0:
                    item.product.is_active = False
                item.product.save()
                
            messages.success(request,'اطلاعات شما با موفقیت ثبت شد','success')
            return render(request,'orders/orderfinal.html', {'order':myorder})
        messages.error(request,'ثیت اطلاعات ناموفق بود','danger')
        return redirect('orders:sender_info', myorder.id)
