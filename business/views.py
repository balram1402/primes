from django.shortcuts import render,redirect
from business.models import towels
from business.models import napkinss
from django.template import loader
from random import shuffle
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def index(request):
    return render(request,"index.html")

def redirect(request):
    return render(request,"index.html")

def towel(request):

    obj= list(towels.objects.all())
    shuffle(obj)
    template = loader.get_template('products.html')
    return render(request, "products.html", {'obj': obj })

def dtowels(request,pro_id):

    objdet = towels.objects.get(pk=pro_id)
    template = loader.get_template('details.html')
    return render(request, "details.html", {'objd': objdet})

def naps(request):

    objnap = list(napkinss.objects.all())
    shuffle(objnap)
    template = loader.get_template('napkins.html')
    return render(request, "napkins.html", {'objn': objnap})

def dnaps(request,nap_id):

    objnapk = napkinss.objects.get(pk=nap_id)
    template = loader.get_template('detailsn.html')
    return render(request, "detailsn.html", {'objnn': objnapk})

def abt(request):

    return render(request,"abtus.html")

def help(request):

    return render(request,"help.html")

def toc(request):

    return render(request,"toc.html")



def searchbar(request):
    input = request.GET.get('search')
    towel_result = towels.objects.filter(Name__icontains=input)
    napkin_result = napkinss.objects.filter(Nname__icontains=input)
    
    

    if towel_result:
        return render(request,"products.html",{'towel_result':towel_result})
    elif napkin_result:
        return render(request,"all.html",{'napkin_result':napkin_result})
    else:
        result = None
        messages.info(request,"No Results for your Search!")
        return render(request,"index.html")

        




def chaddars(request):
    return render(request,"chaddars.html")