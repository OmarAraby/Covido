from django.urls import path , include
from . import views




app_name='detect'

urlpatterns = [

    path('' ,  views.detect , name='detect'),
    #path('result_chest/' ,  views.result_chest , name='result_chest'),
 

]