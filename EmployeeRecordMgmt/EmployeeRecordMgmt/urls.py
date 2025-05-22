"""
URL configuration for EmployeeRecordMgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from employee.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registration', registration, name='registration'),
    path('emp_login', emp_login, name='emp_login'),
    path('emp_home', emp_home, name='emp_home'),
    path('profile', profile, name='profile'),
    path('logout', Logout, name='logout'),
    path('my_experience', my_experience, name='my_experience'),
    path('edit_myexperience', edit_myexperience, name='edit_myexperience'),
    path('my_education', my_education, name='my_education'),
    path('edit_myeducation', edit_myeducation, name='edit_myeducation'),
    path('change_password', change_password, name='change_password'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('emp_view_work_detail/', emp_view_work_detail, name='emp_view_work_detail'),

    path('admin_login', admin_login, name='admin_login'),
    path('admin_home', admin_home, name='admin_home'),
    path('all_employee', all_employee, name='all_employee'),
    path('admin_change_password', admin_change_password, name='admin_change_password'),
    path('edit_profile/<int:id>/',edit_profile, name='edit_profile'),
    path('admin_delete_employee/<int:id>/',admin_delete_employee, name='admin_delete_employee'),
    path('view-current-work/', view_all_employee_current_work, name='view_current_work'),
    path('admin_edit_work_profile/<int:user_id>/', admin_edit_work_profile, name='admin_edit_work_profile'),
    path('employee_list', employee_list, name='employee_list'),
    path('admin_edit_education/<int:pid>/',admin_edit_education, name='admin_edit_education'),
    path('admin_edit_experience/<int:pid>/',admin_edit_experience, name='admin_edit_experience'),
    


]
