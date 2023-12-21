from django.db import models

# Create your models here.

CHOISE_STATE=((
    ('Dhaka','Dhaka'),
    ("Chattagram",'Chattagram'),
    ("Sylhet",'Sylhet'),
    ("Rongpur",'Rongpur'),
    ("Rajshahi",'Rajshahi'),
))

class Profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    created_at=models.DateField(auto_now=False,auto_now_add=False)
    state=models.CharField(choices=CHOISE_STATE,max_length=100 )
    gender=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profile_image',blank=True)
    filedoc=models.FileField(upload_to='filedoc')