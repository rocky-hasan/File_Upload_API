from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','name','email','created_at','state','gender','location','profile_image','filedoc']