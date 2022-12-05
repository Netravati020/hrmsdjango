"""opd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from user import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

# router= DefaultRouter
# router.register('Employeesapi', views.EmployeesList, basename= 'employee')

# from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('All_Employeesapi/',views.EmployeesList.as_view()),
    path('Employeescreateapi/', views.EmployeesCreate.as_view()),
    path('Employeeapi/<int:pk>/',views.EmployeesRetrive.as_view()),

    path('Employeesupapi/<int:pk>/', views.EmployeesUpdate.as_view()),

    path('Employeeupdateapi/', views.update_emp),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update/', views.EmployeeUpdate.as_view({'put':'update'}),name='update'),
    path('edit/', views.edit)

]
