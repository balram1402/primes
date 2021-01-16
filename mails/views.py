from django.shortcuts import render,redirect
from django.core.mail import send_mail
from business.views import towel,naps


def mailfortows(request):

    curr =  request.META.get('HTTP_REFERER')
    current_user = request.user
    userinfo = "Towel Order has received!" + "Mr. " + current_user.username + " has an interest in Towel " + curr + " "  + current_user.email + " " + current_user.first_name

    send_mail(
        'Towels Online',
        userinfo,
        'smtp.gmail.com',
        ['potabattiram@gmail.com','shriharipotabatti67@gmail.com'],
        fail_silently=False,
    )

    return towel(request)


def mailfornaps(request):

    curr =  request.META.get('HTTP_REFERER')
    current_user = request.user
    userinfo =  "Napkin Order has received" + "Mr. " + current_user.username + " has an interest in Napkin " + curr +" " + current_user.email + " " + current_user.first_name



    send_mail(
        'Towels Online',
        userinfo,
        'smtp.gmail.com',
        ['potabattiram@gmail.com','shriharipotabatti67@gmail.com'],
        fail_silently=False,
    )


    return naps(request)

