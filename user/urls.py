from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register17/',views.register,name = "register"),
    path('login17/',views.loginUser,name = "login"),
    path('logout/',views.logout,name = "logout"),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('update/<int:id>',views.update,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    


]