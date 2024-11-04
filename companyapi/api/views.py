

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Company,Employee
from .serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        company=Company.objects.get(pk=pk)
        print(company)
        employees=Employee.objects.filter(company=company)
        emps_serialiser = EmployeeSerializer(employees,many=True,context={'request':request})
        return Response(emps_serialiser.data)

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
