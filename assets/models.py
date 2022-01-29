from django.db import models
from datetime import datetime, date
from django.db.models.fields import CharField
from django.contrib.auth import authenticate

# Create your models here.
class Asset(models.Model):
    assetid = CharField(max_length=100)
    assetname = CharField(max_length=100)
    asset_make = CharField(max_length=100)
    asset_model = CharField(max_length=100)
    slno = CharField(max_length=100)
    dept = CharField(max_length=100)
    pmdone = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    pmdue = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    pmstat = CharField(max_length=100)
    caldue = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    caldone = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    calstat = CharField(max_length=100)
    wrstart = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    wrend = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    warranty = CharField(max_length=100)
    mcstart = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    mcend = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    amc_cmc = CharField(max_length=100)
    stat = CharField(max_length=100)
    

    

    def save(self,*arg,**kwargs):

        if self.caldue>date.today():
            self.calstat = "NOT DUE"
        else:
            self.calstat = "OVER DUE"

        if self.pmdue>date.today():
            self.pmstat = "NOT DUE"
        else:
            self.pmstat = "OVER DUE"
            
        super(Asset,self).save(*arg,**kwargs)