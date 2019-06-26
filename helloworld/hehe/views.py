from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hehe import models
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def h_login(request):
    message = {

    }
    return render(request,'login.html',message)
