from django.urls import path , include
from . import views




app_name='forecast'

urlpatterns = [

    path('' ,  views.forecast , name='forecast'),
 

]