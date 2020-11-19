from django.urls import path
from form1 import views

urlpatterns = [
     path('', views.index , name = 'index'),
     path('authentication-register', views.register , name = 'authentication-register'),
    path('authentication-login', views.signin , name = 'authentication-login'),
    path('report_form', views.report_form , name = 'report_form'),
    path('logout', views.logout,name='logout'),

]
