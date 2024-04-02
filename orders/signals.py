from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order,Senderinfo




def create_senderinfo(sender,**kwargs):
    Senderinfo.objects.create(order=kwargs['instance'])

post_save.connect(receiver=create_senderinfo,sender=Order)






