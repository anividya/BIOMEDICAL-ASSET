from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('asset_insert',views.asset_form,name='asset_insert'),
    path('asset_list',views.index,name='asset_list'),
    path('<int:id>/',views.asset_form,name='asset_update'),
    
]