from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets 
from rest_framework.response import  Response 
from api.models import Company
from api.models import Employee
from api.serializers import CompanySerializer
from api.serializers import EmployeeSerializer
from rest_framework.decorators import action

# Create your views here.
def home_page(request):
    print("this function runs successfully")
    friends=[
        'ankit',
        'ravi',
        'uttam',

    [
        'tomato',
        'potato',
        'cherry',
    ]]
    print(friends[3][0])
    return JsonResponse(friends, safe=False)

def new_page(request):
    print("this is a new page ")
    pass
def home_new(request):
    pass
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class=CompanySerializer

    @action(detail=True, methods=['get'])

    def employees(self,request , pk=None):
        print("get employees of " , pk , "company")
        company=Company.objects.get(pk=pk)
        emps=Employee.objects.filter(company=company)
        emps_serializer=EmployeeSerializer(emps, many=True ,context={'request':request } )
        return Response(emps_serializer.data)
        


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer
    
