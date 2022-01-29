from assets.decorators import allowed_users
from assets.models import Asset
from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AssetForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Asset
from .filters import AssetFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import CalFilter
from datetime import datetime, date, timedelta
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def loginpage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')
            return render(request, 'login.html')
    
    else:
        return render(request, "login.html")

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/login/")
def index(request):
    Asset.objects.filter(pmdue__lte= date.today()).update(pmstat="OVER DUE")
    Asset.objects.filter(pmdue__gte= date.today()).update(pmstat="NOT DUE")
    Asset.objects.filter(caldue__lte= date.today()).update(calstat="OVER DUE")
    Asset.objects.filter(caldue__gte= date.today()).update(calstat="NOT DUE")
    Asset.objects.filter(mcend__lte= date.today()).update(amc_cmc="CONTRACT DUE")
    Asset.objects.filter(mcend__gte= date.today()).update(amc_cmc="UNDER CONTRACT")
    assetlist = Asset.objects.all()
    return render(request, 'assetlist.html', {'index':assetlist})


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['staff'])
def asset_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = AssetForm()
        else:
            assetcontent = Asset.objects.get(pk=id)
            form = AssetForm(instance=assetcontent)
        return render(request, "assetform.html", {'form':form})
    else:
        if id == 0:
            form = AssetForm(request.POST)
        else:
            assetcontent = Asset.objects.get(pk=id)
            form = AssetForm(request.POST,instance=assetcontent)
        if form.is_valid():
            form.save()
        return redirect('asset_list')

@login_required(login_url="/login/")
def asset_view(request):
    assetlist = Asset.objects.all()
    myFilter = AssetFilter(request.GET, queryset=assetlist)
    return render(request, 'pm.html', {'filter':myFilter,'index':assetlist})

@login_required(login_url="/login/")
def calfilter(request):
    assetlist = Asset.objects.all()
    myFilter = CalFilter(request.GET, queryset=assetlist)
    return render(request, 'cal.html', {'filter':myFilter, 'index':assetlist})

