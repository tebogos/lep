from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Firm


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="firm:user-detail")
    class Meta:
        model = Firm
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="firm:group-detail")
    class Meta:
        model = Group
        fields = ('url', 'name')

class FirmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firm
        fields = ('firm_no', 'firm_name','firm_contact','firm_email')