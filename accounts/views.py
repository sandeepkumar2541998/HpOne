from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"emai-id exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
                user.save()
                messages.info(request,"user created")
                subject = 'welcome to HpOne. We are happy to help you!'
                message = f'hi {user.username} thaks for connecting with us.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email,]
                send_mail(subject,message,email_from,recipient_list)
                return redirect('login')
        else:
            messages.info(request,"password not matching.")
            return redirect('register')
    else:

        return render(request,'accounts/register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

