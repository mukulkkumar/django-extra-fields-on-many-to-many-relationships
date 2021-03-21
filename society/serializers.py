from rest_framework import serializers
from .models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'members')


class MembershipSerializer(serializers.ModelSerializer):
    person_name = serializers.CharField(source='person.name')

    class Meta:
        model = Membership
        fields = ('person', 'person_name')
