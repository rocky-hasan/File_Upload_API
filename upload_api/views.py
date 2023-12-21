from django.shortcuts import render
from rest_framework.response import Response
from upload_api.serializers import ProfileSerializers
from rest_framework.views import APIView
from rest_framework import status
from upload_api.models import Profile
from upload_api.forms import ProfileForm
# Create your views here.

class ProfileApiView(APIView):
    def get(self, request, format=None):
        candidates = Profile.objects.all()
        form = ProfileForm()
        return render(request, 'upload.html', {'candidates': candidates, 'form': form})

    def post(self, request, format=None):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'uploadsuccess.html', {'msg': 'File Upload Successfully'})
        return Response({'status': 'Error', 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)






# class ProfileApiView(APIView):
#     def post(self,request,format=None):
#         serializer=ProfileSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'File Upload Successfully','status':'Success','candidate':serializer.data},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
#     def get(self,request,format=None):
#         candidates=Profile.objects.all()
#         serializer=ProfileSerializers(candidates, many=True)
#         return Response({'status':'Success','candidate':serializer.data},status=status.HTTP_200_OK)

