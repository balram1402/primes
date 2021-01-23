from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from business.views import index
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views import View
import math, random
from django.http import HttpResponse


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if '@' not in email and '.' not in email :
            messages.info(request, "Invalid Email")
            return render(request, "register.html")
        else:
            if len(first_name) != 10:
                messages.info(request,"Enter Valid Phone Number")
                return render(request,"register.html")
            else:

                if password1 == password2:
                    if User.objects.filter(username=username).exists():
                        messages.info(request, "Username Exists,Try Different!")
                        return render(request, "register.html")

                    else:

                        if User.objects.filter(email=email).exists():
                            messages.info(request, "Email Already Exists,you may Login to your account")
                            return render(request, "register.html")


                        else:
                            if User.objects.filter(first_name=first_name).exists():
                                messages.info(request,"Phone Number Exists, Try Different One!")
                                return render(request,"register.html")


                            else:
                   
                                message = "Welcome to Towels Online" + "\n \nTowels Online is an Online Shopping Platform where one can order bulk quantity products in wholesale prices. We are glad to see you here.\nCheck out our new products on the website, add in Enquiry list for Interested Products,\nwe will get in touch with you soon. \nThank You! "
                               
                                subject = 'Hello, '+ (username)
                                send_mail(
                                    subject,
                                    message,
                                    'smtp.gmail.com',
                                    [email],
                                    fail_silently=False,
                                )


                                
                                user = User.objects.create_user(username=username, email=email, first_name=first_name, password=password1)
                                user.save();
                                return login(request)
                                

                else:
                    messages.info(request, "Non-matching passwords,Try Again!")
                    return render(request, "register.html")


    else:
        return render(request, "register.html")

        
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"index.html")
        else:

            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

