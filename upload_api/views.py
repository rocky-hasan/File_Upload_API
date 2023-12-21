from django.shortcuts import render
from rest_framework.response import Response
from upload_api.serializers import ProfileSerializers
from rest_framework.views import APIView
from rest_framework import status
from upload_api.models import Profile
# Create your views here.

class ProfileApiView(APIView):
    def post(self,request,format=None):
        serializer=ProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'File Upload Successfully','status':'Success','candidate':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def get(self,request,format=None):
        candidates=Profile.objects.all()
        serializer=ProfileSerializers(candidates, many=True)
        return Response({'status':'Success','candidate':serializer.data},status=status.HTTP_200_OK)

