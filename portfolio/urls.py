from django.contrib import admin
from django.urls import path
from django.conf.urls import handler400, handler500
from . import views
app_name = "portfolio"

urlpatterns = [
    
    path('architecture/',views.ArchPort,name='architecture'),
    path('software/',views.SoftwarePort,name='software'),
    # path('<int:id>/',views.post,name='post'),
    
]