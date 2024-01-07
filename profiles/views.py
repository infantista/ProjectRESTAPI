from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('id')  
    serializer_class = ProfileSerializer

def index(request):
    return render(request,'index.html')
