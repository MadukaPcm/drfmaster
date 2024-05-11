
from django.contrib import admin
from django.urls import path
from rest_framework import routers 

routers = routers.DefaultRouter() 

urlpatterns = routers.urls 


urlpatterns = [
    path('admin/', admin.site.urls),
]
