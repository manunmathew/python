from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint
from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=10,null=True,blank=True)

    def generate_otp(self):
        otp_num = str(randint(1000,9000))+str(self.id)
        self.otp = otp_num
        self.save()

class Profile(models.Model):
    owner= models.OneToOneField(User,on_delete=models.CASCADE,related_name="userprofile")
    address= models.TextField(null=True)
    bio=models.CharField(max_length=200,null=True)
    picture=models.ImageField(upload_to="profilepicture",null=True,blank=True,default="profilepicture/default.png")


#instance = object
#created=True|False
#after created
#signals => post_save(),pre_save(),post_init(),pre_init()

def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile,User)
