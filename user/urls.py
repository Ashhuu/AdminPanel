from django.urls import path
from . import views

urlpatterns = [
    path('register/admin', views.registerView, name='Register'),
    path('', views.loginView, name='Login'),
    path('dashboard/', views.dashboardView, name='Dashboard'),
    path('dashboard/register/', views.adminRegister, name='AdminReg'),
    path('error404/', views.errorView, name='error404'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/user/', views.adminDetails, name='Details'),
    path('dashboard/user/delete/(?P<id>\w+)', views.deleteView, name='Delete'),
    path('dashboard/user/edit/(?P<id>\w+)', views.editView, name='Edit'),
]


