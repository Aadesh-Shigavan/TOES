from django.shortcuts import render
import datetime

# Create your views her

def getin( request):
    return render( request , 'Sign/res.html')


def sign_in(request):
    return render(request , 'Sign/sign_in.html')


def sign_up(request):
    return render(request , 'Sign/sign_up.html')


def forget_pass(request):
    return render( request , 'Sign/forget_pass.html')

def home(request):

        dt=datetime.datetime.now();
        t = datetime.datetime.now().time();
        d={
           'dates':dt,
           'time' : t ,

        }
        return render(request, 'Sign/home.html',context=d)

def phone(request):
    return render(request , 'Sign/phone.html')

def workers(request):
    return render(request , 'Sign/workers.html')

def recruiters(request):
    return render(request , 'Sign/recruiters.html')
