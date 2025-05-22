from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import EmployeeDetail,EmployeeEducation,EmployeeExperience
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .filters import EmployeeDetailFilter

def index(request):
    return render(request, 'index.html')

def registration(request):
    error = " "
    if request.method == "POST":
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        ec = request.POST.get('empcode')
        em = request.POST.get('email')
        pwd = request.POST.get('pwd')

        try:
            # # Check if a user with this email already exists
            if User.objects.filter(username=em).exists():
                error = "An account with this email already exists."
                return render(request, 'registration.html', locals())

            # Create the User object
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)

            # Create the EmployeeDetail object and link it to the User
            EmployeeDetail.objects.create(user=user, empcode=ec)

            # Create the EmployeeEducation object and link it to the User
            EmployeeEducation.objects.create(user=user)

            # Create the EmployeeExperience object and link it to the User
            EmployeeExperience.objects.create(user=user)

            error = "no"  # Success"""


        except:
            error = "yes"
    return render(request, 'registration.html', locals())


def emp_login(request):
    error = " "
    if request.method =="POST":
        u=request.POST.get('emailid')
        p=request.POST.get('password')
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    
    return render(request, 'emp_login.html',locals())



def emp_home(request):

    # This function checks whether the user making the request is
    # authenticated (logged in). If the user is not authenticated, 
    # they are redirected to the login page (emp_login). Otherwise, 
    # the function renders the emp_home.html template.

    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')

def Logout(request):
    # logout(request)  used to destroy the all session variables created by user login
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user

    try:
        employee = EmployeeDetail.objects.get(user=user)
    except EmployeeDetail.DoesNotExist:
        messages.error(request, "Profile details not found. Please contact admin.")
        return redirect('emp_home')  # or another appropriate view

    if request.method == "POST":
        # Fetch values from form
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        ec = request.POST.get('empcode')
        dept = request.POST.get('department')
        designation = request.POST.get('designation')
        contact = request.POST.get('contact')
        jdate = request.POST.get('jdate')
        gender = request.POST.get('gender')

        # Update the employee profile
        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'profile.html', locals())

# def admin_login(request):
#     return render(request, 'admin_login.html')


def my_experience(request):

    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = " "

    # identify the current user
    user = request.user

    # takes current user/employee all experience deatils and store in experience variable
    experience=EmployeeExperience.objects.get(user=user)

    return render(request, 'my_experience.html', locals())



def edit_myexperience(request):

    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = " "
    user = request.user

     # takes current user/employee all experience deatils and store in experience variable
    experience=EmployeeExperience.objects.get(user=user)

    if request.method == "POST":

        #fetch values from experience section
        company1name = request.POST.get('company1name')
        company1desig = request.POST.get('company1desig')
        company1salary = request.POST.get('company1salary')
        company1duration = request.POST.get('company1duration')
        
        company2name = request.POST.get('company2name')
        company2desig = request.POST.get('company2desig')
        company2salary = request.POST.get('company2salary')
        company2duration = request.POST.get('company2duration')

        company3name = request.POST.get('company3name')
        company3desig = request.POST.get('company3desig')
        company3salary = request.POST.get('company3salary')
        company3duration = request.POST.get('company3duration')

        #updates values of experience section
        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error = "no" 
        except:
            error = "yes"
    return render(request, 'edit_myexperience.html', locals())


def my_education(request):

    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = " "

    # identify the current user
    user = request.user

    # takes current user/employee all education deatils and store in education variable
    education=EmployeeEducation.objects.get(user=user)

    return render(request, 'my_education.html', locals())



def edit_myeducation(request):

    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = " "
    user = request.user

     # takes current user/employee all experience deatils and store in experience variable
    education=EmployeeEducation.objects.get(user=user)

    if request.method == "POST":

        #fetch values from experience section
        coursepg = request.POST.get('coursepg')
        schoolclgpg = request.POST.get('schoolclgpg')
        yearofpassingpg = request.POST.get('yearofpassingpg')
        percentagepg = request.POST.get('percentagepg')
        
        coursegra = request.POST.get('coursegra')
        schoolclggra = request.POST.get('schoolclggra')
        yearofpassinggra = request.POST.get('yearofpassinggra')
        percentagegra = request.POST.get('percentagegra')

        coursehsc = request.POST.get('coursehsc')
        schoolclghsc = request.POST.get('schoolclghsc')
        yearofpassinghsc = request.POST.get('yearofpassinghsc')
        percentagehsc = request.POST.get('percentagehsc')

        coursessc = request.POST.get('coursessc')
        schoolclgssc = request.POST.get('schoolclgssc')
        yearofpassingssc = request.POST.get('yearofpassingssc')
        percentagessc = request.POST.get('percentagessc')

        #updates values of education section
        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        try:
            education.save()
            error = "no"  # Success"""
        except:
            error = "yes"
    return render(request, 'edit_myeducation.html', locals())


def change_password(request):

    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = " "
    user = request.user

    if request.method == "POST":

        c = request.POST.get('currentpassword')
        n = request.POST.get('newpassword')

        try:
            # checks user's current login password is same as currentpassword variable. and if it matches, it will change the current password with newpassword
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no" 
            else:
                error = "not_match"
        except:
            error = "yes"
    return render(request, 'change_password.html', locals())


@csrf_exempt
def forgot_password(request):
    if request.method == 'GET':
        return render(request, 'forgot_password.html')  # Show form

    elif request.method == 'POST':
        username = request.POST.get('username')
        empcode = request.POST.get('empcode')
        new_password = request.POST.get('new_password')

        if not all([username, empcode, new_password]):
            return render(request, 'forgot_password.html')

            # return JsonResponse({'error': 'All fields are required.'}, status=400)

        try:
            user = User.objects.get(username=username)
            employee = EmployeeDetail.objects.get(user=user)

            if employee.empcode != empcode:
                return render(request, 'forgot_password.html')
                # return JsonResponse({'error': 'Empcode does not match.'}, status=400)

            user.set_password(new_password)
            user.save()
            return render(request, 'emp_login.html')
            # return JsonResponse({'success': 'Password updated successfully.'})

        except User.DoesNotExist:
            return render(request, 'registration.html')
        except EmployeeDetail.DoesNotExist:
            return render(request, 'registration.html')
    else:
        return JsonResponse({'error': 'Only GET and POST methods allowed.'}, status=405)
    

def emp_view_work_detail(request):

    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = " "

    # identify the current user
    user = request.user

    # takes current user/employee all education deatils and store in education variable
    employee=EmployeeDetail.objects.get(user=user)

    return render(request, 'emp_view_work_detail.html', locals())



# ADMIN SECTION PART



def admin_login(request):
    error = " "
    if request.method =="POST":
        u=request.POST.get('username')
        p=request.POST.get('pwd')
        user = authenticate(username=u,password=p)
        if user is not None and user.is_staff:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    
    return render(request, 'admin_login.html',locals())


def admin_home(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def all_employee(request):

    user = request.user

    if not user.is_authenticated:
        return redirect('admin_login')
    
    employee = EmployeeDetail.objects.all()

    return render(request, 'all_employee.html',locals())



def admin_change_password(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    error = " "
    user = request.user

    if request.method == "POST":

        c = request.POST.get('currentpassword')
        n = request.POST.get('newpassword')

        try:
            # checks user's current login password is same as currentpassword variable. and if it matches, it will change the current password with newpassword
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no" 
            else:
                error = "not_match"
        except:
            error = "yes"
    return render(request, 'admin_change_password.html', locals())




def edit_profile(request, id):

    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    user = request.user
    employee = EmployeeDetail.objects.get(id=id)

    if request.method == 'POST':
        # Update user model
        user = employee.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.save()

        # Update employee model
        employee.contact = request.POST.get('contact')
        employee.gender = request.POST.get('gender')
        employee.save()

        return redirect('all_employee')  # Use your actual view name


    return render(request, 'admin_employee_edit_profile.html', locals())
    # return render(request, 'edit_profile.html', {'employee': employee, 'user': user})


def admin_delete_employee(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    # Safely get the employee or raise 404
    employee = get_object_or_404(EmployeeDetail, pk=id)
    employee.delete()
    print(f"Employee with employee id {id} deleted successfully..")

    # Fetch updated list of employees
    employee_list = EmployeeDetail.objects.all()

    return render(request, 'all_employee.html', {'employee': employee_list})


def view_all_employee_current_work(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('admin_login')
    
    employee = EmployeeDetail.objects.all()

    return render(request, 'admin_view_work.html',locals())



def admin_edit_work_profile(request, user_id):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    try:
        user = User.objects.get(id=user_id)
        employee = EmployeeDetail.objects.get(user=user)
    except (User.DoesNotExist, EmployeeDetail.DoesNotExist):
        # Optional: handle not found
        return redirect('all_employee')  # or show a 404 page

    if request.method == 'POST':
        # Update User model
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        # Update Employee model
        employee.empcode = request.POST.get('empcode')
        employee.empdept = request.POST.get('empdept')
        employee.designation = request.POST.get('designation')
        employee.salary = request.POST.get('salary')
        employee.joiningdate = request.POST.get('joiningdate')
        employee.save()

        # return redirect('admin_edit_work_profile', user_id=user.id)
        return redirect('all_employee')

    return render(request, 'admin_edit_work_profile.html', {'employee': employee})




def employee_list(request):
    employee_filter = EmployeeDetailFilter(request.GET, queryset=EmployeeDetail.objects.all())
    return render(request, 'employee_list.html', {'filter': employee_filter})




def admin_edit_education(request,pid):

    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = " "

    # take the current selected user with user id
    user=User.objects.get(id=pid)
     # takes current user/employee all experience deatils and store in education variable
    education=EmployeeEducation.objects.get(user=user)

    if request.method == "POST":

        #fetch values from experience section
        coursepg = request.POST.get('coursepg')
        schoolclgpg = request.POST.get('schoolclgpg')
        yearofpassingpg = request.POST.get('yearofpassingpg')
        percentagepg = request.POST.get('percentagepg')
        
        coursegra = request.POST.get('coursegra')
        schoolclggra = request.POST.get('schoolclggra')
        yearofpassinggra = request.POST.get('yearofpassinggra')
        percentagegra = request.POST.get('percentagegra')

        coursehsc = request.POST.get('coursehsc')
        schoolclghsc = request.POST.get('schoolclghsc')
        yearofpassinghsc = request.POST.get('yearofpassinghsc')
        percentagehsc = request.POST.get('percentagehsc')

        coursessc = request.POST.get('coursessc')
        schoolclgssc = request.POST.get('schoolclgssc')
        yearofpassingssc = request.POST.get('yearofpassingssc')
        percentagessc = request.POST.get('percentagessc')

        #updates values of education section
        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        try:
            education.save()
            error = "no"  # Success"""
        except:
            error = "yes"
    return render(request, 'admin_edit_education.html', locals())



def admin_edit_experience(request,pid):

    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = " "
    # take the current selected user with user id
    user=User.objects.get(id=pid)
     # takes current user/employee all experience deatils and store in experience variable
    experience=EmployeeExperience.objects.get(user=user)

    if request.method == "POST":

        #fetch values from experience section
        company1name = request.POST.get('company1name')
        company1desig = request.POST.get('company1desig')
        company1salary = request.POST.get('company1salary')
        company1duration = request.POST.get('company1duration')
        
        company2name = request.POST.get('company2name')
        company2desig = request.POST.get('company2desig')
        company2salary = request.POST.get('company2salary')
        company2duration = request.POST.get('company2duration')

        company3name = request.POST.get('company3name')
        company3desig = request.POST.get('company3desig')
        company3salary = request.POST.get('company3salary')
        company3duration = request.POST.get('company3duration')

        #updates values of experience section
        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error = "no" 
        except:
            error = "yes"
    return render(request, 'admin_edit_experience.html', locals())


