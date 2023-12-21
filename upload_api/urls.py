
from django.urls import path
from upload_api.views import ProfileApiView
urlpatterns = [
    path('fileupload/', ProfileApiView.as_view(),name='fileupload'),
    path('filelist/', ProfileApiView.as_view(), name='profile-api'),
]