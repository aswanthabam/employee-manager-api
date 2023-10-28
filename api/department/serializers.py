# apps/management/api/serializers.py

from rest_framework import serializers,validators
from ..models import *

"""
User Serializer
"""
class DepartmentSerializer(serializers.ModelSerializer):
    department_id = serializers.ReadOnlyField()

    def create(self, validated_data):
        org = self.context.get('organization')
        validated_data['organization'] = org
        return Department.objects.create(**validated_data)
    class Meta:
        model = Department
        fields = ['department_id','name','location','manager']

class DepartmentUpdateSerializer(serializers.ModelSerializer):
    department_id = serializers.ReadOnlyField()
    name = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    manager = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):  
        instance.name = validated_data.get('name',instance.name)
        instance.location = validated_data.get('location',instance.location)
        manager = validated_data.get('manager',None)
        if manager != None:
            manager = Employee.objects.filter(employee_id=manager).first()
            instance.manager = manager
        instance.save()  
        return instance  
    class Meta:
        model = Department
        fields = ['department_id','name','location','manager']

