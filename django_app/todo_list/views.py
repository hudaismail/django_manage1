from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
import json
#from .utils import cookieCart, cartData, guestOrder
import datetime
from django.contrib import messages
from django.core.mail import send_mail


from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid


# Create your views here.

def index(request):

    return render(request, 'index.html')

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        product= Products.objects.filter(name__contains=searched)
        return render(request, 'search.html',{'searched':searched,'product':product})
    else:
        return render(request,'search.html',{})


def category(request,foo):
    #data = cartData(request)
    #cartItems = data['cartItems']
    #order = data['order']
    #items = data['items']
    #, 'items': items, 'order': order, 'cartItems': cartItems

    # replace hyphens with spaces
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Products.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, ("That category dosn't exist"))
        return redirect('index')

def home(request):
    ducts = Products.objects.all()

    return render(request, 'home.html',{'ducts':ducts})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
           New message :{}
           From :{}
           '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['enghudaismail@gmail.com'])
        reply_to = [email]
        print('send Success')
        return HttpResponse("email send Successfully")

    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html')
