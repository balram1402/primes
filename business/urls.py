from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('redirect/',views.redirect,name='redirect'),
    path('towel/',views.towel,name='towel'),
    path('dtowels/<int:pro_id>/',views.dtowels,name='dtowels'),
    path('naps/',views.naps,name='naps'),
    path('dnaps/<int:nap_id>/',views.dnaps,name='dnaps'),
    path('abt/',views.abt,name='abt'),
    path('help/',views.help,name='help'),
    path('toc/',views.toc,name='toc'),
    path('searchbar/',views.searchbar,name='searchbar'),

]

