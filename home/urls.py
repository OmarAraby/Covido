from django.urls import path , include
from . import views
from contact.views import about



app_name='home'

urlpatterns = [
    
    path('' ,  views.home , name='home'),
    path('detect/' ,  views.detect , name='detect'),
    path('prevention/' ,  views.prevention , name='prevention'),
    path('faqs/' ,  views.faqs , name='faqs'),
    path('about/' , about , name='about'),

]