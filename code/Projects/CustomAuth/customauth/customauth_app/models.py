from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=10,null=True,blank=True)

    def generate_otp(self):
        otp_num = str(randint(1000,9000))+str(self.id)
        self.otp = otp_num
        self.save()
