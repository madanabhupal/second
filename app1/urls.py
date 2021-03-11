from django.urls import path
app_name='app1'
from app1 import views
urlpatterns=[
    path('madhan/',views.madhan,name='madhan'),
    
    ]
