from assets.models import Asset
from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AssetForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Asset
from .filters import AssetFilter
from .filters import CalFilter



# Create your views here.
def index(request):
    assetlist = Asset.objects.all()
    myFilter = AssetFilter(request.GET, queryset=assetlist)
    assetcontent = {"index":Asset.objects.all()}
    return render(request, 'assetlist.html', {'filter':myFilter, 'index':assetlist})

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

def asset_view(request):
    assetlist = Asset.objects.all()
    myFilter = AssetFilter(request.GET, queryset=assetlist)
    return render(request, 'pm.html', {'filter':myFilter,'index':assetlist})

def calfilter(request):
    assetlist = Asset.objects.all()
    myFilter = CalFilter(request.GET, queryset=assetlist)
    return render(request, 'cal.html', {'filter':myFilter, 'index':assetlist})

