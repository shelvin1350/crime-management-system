"""crime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crimeapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name="home page"),
    path('', views.home,name="home page"),
    path('adminhome/', views.adminhome,name="adminhome page"),
    path('userhome/', views.userhome,name="userhome page"),
    path('dgphome/', views.dgphome,name="dgphome page"),
    path('userreg/', views.userreg,name="userreg page"),

    path('complaint/', views.complaint,name="complaint page"),
    path('stationreg/', views.stationreg,name="stationreg page"),
    path('adminsendfilestation/', views.adminsendfilestation,name="adminsendfilestation page"),

    path('login/', views.login,name="login page"),
    path('stationviewcomplaint/', views.stationviewcomplaint,name="stationviewcomplaint page"),
    path('adminapprovecomp/', views.adminapprovecomp,name="adminapprovecomp page"),
    path('adminviewprocessing/', views.adminviewprocessing,name="adminviewprocessing page"),
    path('useraddmissingitem/', views.useraddmissingitem,name="useraddmissingitem page"),
    path('stationhome/', views.stationhome,name="stationhome page"),
    path('stationaddcomplaintresponse/', views.stationaddcomplaintresponse,name="stationaddcomplaintresponse page"),
    path('stationaddcrimedetails/', views.stationaddcrimedetails,name="stationaddcrimedetails page"),
    path('stationaddcriminaldetails/', views.stationaddcriminaldetails,name="stationaddcriminaldetails page"),
    path('stationviewmissingitem/', views.stationviewmissingitem,name="stationviewmissingitem page"),
    path('adminsendfilestation/', views.adminsendfilestation,name="adminsendfilestation page"),
    path('stationsendfilestation/', views.stationsendfilestation,name="stationsendfilestation page"),
    path('adminviewfiles/', views.adminviewfiles,name="adminviewfiles page"),
    path('stationviewfiles/', views.stationviewfiles,name="stationviewfiles page"),
    path('dgpviewcriminal/', views.dgpviewcriminal,name="dgpviewcriminal page"),
    path('dgpviewcrime/', views.dgpviewcrime,name="dgpviewcrime page"),
    path('dgpsendfilestation/', views.dgpsendfilestation,name="dgpsendfilestation page"),
    path('stationaddwantedlist/', views.stationaddwantedlist,name="stationaddwantedlist page"),
    path('stationviewcrime/', views.stationviewcrime,name="stationviewcrime page"),
    path('stationviewcriminal/', views.stationviewcriminal,name="stationviewcriminal page"),
    path('userviewwantedlist/', views.userviewwantedlist,name="userviewwantedlist page"),
    path('stationaddmissingresponse/', views.stationaddmissingresponse,name="stationaddmissingresponse page"),
    path('adminviewcriminal/', views.adminviewcriminal,name="adminviewcriminal page"),
    path('adminaddauthority/', views.adminaddauthority,name="adminaddauthority page"),

    path('userviewcomplaintstatus/', views.userviewcomplaintstatus,name="userviewcomplaintstatus page"),
    path('userviewmissingstatus/', views.userviewmissingstatus,name="userviewmissingstatus page"),

]
