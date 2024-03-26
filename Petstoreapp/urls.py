
from django.urls import path,include
from Petstoreapp import views

urlpatterns = [
    path('index',views.index),
    path('',views.index),
    path('about',views.about),
    path('services',views.services),
    path('listproduct',views.listproduct),
    path('petcategory/<id>',views.petcategory),
    path('petdetail/<id>',views.petdetail),
    path('petcategory/petdetail/<id>',views.petdetail),
    path('register',views.register),
    path('handlelogin',views.handlelogin),
    path('handlelogout',views.handlelogout),
    path('forgotpassword',views.forgotpassword),
    path('searchform',views.searchform,name="searchform"),
]
