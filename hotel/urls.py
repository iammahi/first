from django.urls import path
from django.conf.urls import url
from.views import *

urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('order',Order, name='order'),
    path('dashboard/',Dashboard,name='dashboard'),
    path('dashboardStaff/',DashboardStaff,name='staff'),
    path('login/',Loginpage,name='login'),
    path('conform_order',Conform_orders,name='conform_order'),
    path('dashboard/update/<int:pk>/',Update,name='update'),
    path('dashboardStaff/update/<int:pk>/',Update,name='updatestaff'),
    path('dashboard/<str:pk>/',Delete_order,name='remove'),
    path('logout',Logout,name='logout'),
    path('dashboard/items/<int:list>/',Items,name='items'),
    path('dashboard/print/<int:pk>/',Print,name='print'),
    path('recive_message/',Receive_mail,name='print'),

]
