from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect
from .forms import StudentRegistration
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.
def add_show(request):
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
        nm = fm.cleaned_data['name']
        em = fm.cleaned_data['email']
        pm = fm.cleaned_data['password']
        reg = Student(name=nm, email=em, password=pm)
        reg.save()
        fm = StudentRegistration()
    else:
     fm = StudentRegistration() 
    stud = Student.objects.all() 
    return render(request, 'addandshow.html', {'form':fm,'stu':stud})


    #This Function will delete data
def delete_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


#This function will update or edit
def update_data(request,id):
    if request.method == 'POST':
        pi= Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
         pi= Student.objects.get(pk=id)
         fm = StudentRegistration(instance=pi) 
    return render(request, 'updatestu.html',{'form':fm})


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'user is alerady exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name= first_name, last_name=last_name) 
                user.set_password(password)
                user.save()
                return redirect('login_user') 
    else:
        
        
     return render(request, 'register.html') 



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid user')
            return redirect('login_user')
    else : 
        return render(request, 'login.html') 

def logout_user(request):
    logout(request)
    return redirect('home')
    
        
   