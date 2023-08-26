from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from api import views
from api.views import CompanyViewSet
from api.views import EmployeeViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'companies' ,CompanyViewSet)
router.register(r'employees' ,EmployeeViewSet )


urlpatterns = [
    path('new/' , views.home_page ,name="home"),
    path('home_new/', views.home_new, name="home_new"),
    path('router/' , include(router.urls))
    

]
