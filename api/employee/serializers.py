# apps/management/api/serializers.py

from rest_framework import serializers,validators
from ..models import *

"""
User Serializer
"""
class EmployeeSerializer(serializers.ModelSerializer):
    employee_id = serializers.ReadOnlyField()
    user = serializers.CharField(required=False)
    def create(self, validated_data):
        dept = self.context.get('department')
        validated_data['department'] = dept
        user = validated_data.get('user',None)
        if user != None:
            user = CustomUser.objects.filter(username=user).first()
            validated_data['user'] = user
        return Employee.objects.create(**validated_data)
    class Meta:
        model = Employee
        fields = ['employee_id','name','email','contact','date_of_joining','experience','salary','user']

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    employee_id = serializers.ReadOnlyField()
    name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    contact = serializers.CharField(required=False)
    date_of_joining = serializers.DateTimeField(required=False)
    experience = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    user = serializers.CharField(required=False)

    def update(self, instance, validated_data):  
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.contact = validated_data.get('contact',instance.contact)
        instance.date_of_joining = validated_data.get('date_of_joining',instance.date_of_joining)
        instance.experience = validated_data.get('experience',instance.experience)
        instance.salary = validated_data.get('salary',instance.salary)
        user = validated_data.get('user',None)
        if user != None:
            user = CustomUser.objects.filter(username=user).first()
            instance.user = user
        instance.save()  
        return instance  
    class Meta:
        model = Employee
        fields = ['employee_id','name','email','contact','date_of_joining','experience','salary','user']

