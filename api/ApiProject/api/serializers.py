from rest_framework import serializers
from api.models import Company
from api.models import Employee

#create serializers
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    Employee_id=serializers.ReadOnlyField()
    class Meta:
        model= Employee
        fields="__all__"