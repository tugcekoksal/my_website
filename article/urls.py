from django.contrib import admin
from django.urls import path
from django.conf.urls import handler400, handler500
from . import views
app_name = "article"

urlpatterns = [
    
    path('addarticle/',views.addarticle,name = "addarticle"),
    path('',views.blog,name='blog'),
    path('<int:id>/',views.post,name='post'),
    path('comment/<int:id>',views.comment,name='comment'),
    
    
]