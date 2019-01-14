from django.shortcuts import render
from .models import Firm
from .forms import FirmModelForm
from django.views.generic import CreateView

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from  firm.serializers import UserSerializer, GroupSerializer, FirmSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FirmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Create your views here.

class FirmCreateView(CreateView):
    model = Firm
    form_class=FirmModelForm
    template_name = 'firm/create_firm_view.html'
    queryset = Firm.objects.all() 

