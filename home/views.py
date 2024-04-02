from django.shortcuts import render

from products.models import Categories
from django.views import View





class HomeView(View):
    template_name='home/index.html'
    def get(self,request):
        
        return render(request,self.template_name)


# Create your views here.
