from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import FormData
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):

    return render(request , 'index.html')

def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email= email,password= password  )
        user.save()
        messages.success(request, 'Successfully Register! Now Please Login With Your Credentials')
        return redirect("authentication-login")
    return render(request , 'authentication-register1.html')

# def signup(request):

#     if request.method == 'POST':

#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']

#         if password1==password2:

#             if User.objects.filter(username=username).exists():
#                 messages.warning(request, 'This username is already taken')
#                 return redirect("sign_up")
#             elif User.objects.filter(email=email):
#                 messages.warning(request, 'This email is already taken , Please try other one!')
#                 return redirect("sign_up")

#             else:
#                 user = User.objects.create_user(username=username ,password= password1 , email= email ,first_name=first_name , last_name = last_name)
#                 user.save()
#                 messages.success(request, 'Successfully Register! Now Please Login With Your Credentials') 
#                 return redirect("signin")
                    

#         else:
#             messages.warning(request, 'Password is not matching')  
#             return redirect("sign_up")
                
#     else:
        
#         return render(request,'signup.html')

    
def signin(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password )

        if user is not None:
            auth.login(request , user)
            return redirect ("/")

        else:
            
            messages.warning(request, 'Please Enter Valid Username & Password')  
            return redirect ("authentication-login")
    else:
        return render(request,'authentication-login1.html')


def report_form(request):
    if request.method=='POST':
        location1 = request.POST.get('location1')
        department = request.POST.get('department')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location2 = request.POST.get('location2')
        severity = request.POST.get('severity')
        cause = request.POST.get('cause')
        action = request.POST.get('action')
        env = request.POST.get('env')
        injury = request.POST.get('injury')
        property1 = request.POST.get('property1')
        vehicle = request.POST.get('vehicle')

        data = FormData(location1=location1,location2=location2,Description=department,date=date,time=time,severity=severity,cause=cause,actions=action,type_env=env,type_inju=injury,type_property=property1,type_vehicle=vehicle)
        data.save()
        messages.success(request, 'Incident Submitted Successfully')  
        return redirect('/')
    return render(request , 'report_form.html')


def logout(request):

    auth.logout(request)
    return redirect("/")