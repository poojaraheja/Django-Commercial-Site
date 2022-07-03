from datetime import datetime
from django.shortcuts import render
from home.models import Contact
import email
from multiprocessing import context
from urllib.request import Request
from django.contrib import messages


def index(request):
    context = {
        "variable1":"pooja is great",
        "variable2":"upr wali line galat h"
    }
    #messages.success(request, "hiiiii")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('this is aboutpage')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse('this is services')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contacts = Contact(name= name, email= email, phone= phone, desc= desc, date= datetime.today())
        contacts.save()
        messages.success(request, 'Your message has been sent !!')

    
    return render(request, 'contact.html')
    #return HttpResponse('this is contact')