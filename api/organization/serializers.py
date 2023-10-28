# apps/management/api/serializers.py

from rest_framework import serializers,validators
from ..models import *

"""
User Serializer
"""
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['organization_id','name','email','contact','address']
    
    organization_id = serializers.ReadOnlyField()

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user
        return Organization.objects.create(**validated_data)  
class OrganizationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['organization_id','name','email','contact','address']
    name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    contact = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    organization_id = serializers.ReadOnlyField()
    def update(self, instance, validated_data):  
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.contact = validated_data.get('contact',instance.contact)
        instance.address = validated_data.get('address',instance.address)
        instance.save()  
        return instance  
    
