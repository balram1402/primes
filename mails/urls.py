from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.mailfortows,name='mailfortows'),
    path('mailfornaps/',views.mailfornaps,name='mailfornaps'),


]