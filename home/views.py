from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render





def index(request):

    context={
        'page':'home'
             }
    return render(request,'index.html',context)

