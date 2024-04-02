from celery import shared_task

from datetime import timedelta,datetime
from .models import OtpCode
import pytz


@shared_task
def remove_expire_otp_code():
    expired_time=datetime.now(tz=pytz.timezone('Asia/tehran'))- timedelta(minutes=1)
    OtpCode.objects.filter(created__lt=expired_time).delete()