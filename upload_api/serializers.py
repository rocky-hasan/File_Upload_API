from rest_framework import serializers
from upload_api.models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields=['id','name','email','created_at','state','gender','location','profile_image','filedoc']
        
