from django.contrib import admin
from django.urls import path
from .views import addnewproduct, cartview, crudtable, crudtabledelete, crudtableupdate, forgotpassword, home, login, logout , about, removefromcart, signup, updatepassword, updateproimg, view

urlpatterns = [
    path('home/',home ,name="home"),
    path('about/',about ,name="about"),
    path('signup/',signup ,name="signup"),
    path('login/',login ,name="login"),
    path('crudtable/',crudtable,name="crudtable"),
    path('crudtable/delete/<int:pk>', crudtabledelete, name="crudtabledelete"),
    path('crudtable/update/<int:pk>', crudtableupdate, name="crudtableupdate"),
    path('crudtable/addnewproduct/',addnewproduct, name="addnewproduct"),
    path('crudtable/updateimage/',updateproimg,name="updateproimg"),
    path('home/view/<int:pk>',view, name="view"),
    path('logout/',logout,name="logout"),
    path('forgotpassword/',forgotpassword,name="forgotpassword"),
    path('forgotpassword/updatepassword/<str:username>',updatepassword,name="updatepassword"),
    path('cartview/',cartview, name="cartview"),
    path('cart/delete/<int:pk>',removefromcart,name="removefromcart")
]