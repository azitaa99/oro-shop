from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product,Comment,Categories
from django.views.generic.edit import FormMixin
from .forms import commentForm,replyForm,addform
from django.urls import reverse,reverse_lazy
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin



class productview(View):
    def get(self, request,category_slug=None):
        products=Product.objects.all()
        category=Categories.objects.all()
        if category_slug:
            mycategory=Categories.objects.get(slug=category_slug)
            products=Product.objects.filter(categories=mycategory)
        return render(request,'products/products.html',{'products':products,'category':category} )







class productDetail(FormMixin,DetailView):
    model = Product
    template_name = 'products/detail.html'
    form_class = commentForm
    replyform_class=replyForm
    addform_class=addform
    context_object_name='product'


    def get_queryset(self):
        id=self.kwargs['pk']
        product=Product.objects.get(pk=id)
        if product.quantity <= 0:
            product.quantity=0
            product.is_active=False
            product.save()
        return super().get_queryset()

    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        context['form']=self.form_class
        context['replyform']=self.replyform_class
        context['addform']=self.addform_class
        return context

    def get_success_url(self):
        return reverse_lazy('products:products_detail', kwargs={'pk': self.object.pk})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
    
        if form.is_valid():
            mycomment=form.save(commit=False)
            mycomment.user=self.request.user 
            mycomment.product=self.object
            mycomment.save()
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
       

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class createreply(LoginRequiredMixin,View):
    form_class=replyForm
    def post(self, request,product_id,comment_id):
        form=self.form_class(request.POST)
        comment=Comment.objects.get(pk=comment_id)
        product=get_object_or_404(Product,pk=product_id)
    
        if form.is_valid():
            reply=form.save(commit=False)
            reply.user=request.user
            reply.product=product
            reply.reply=comment
            reply.is_reply=True
            reply.save()
        return redirect('products:products_detail',   comment.product.id)
        
   
    
        


# Create your views here.
