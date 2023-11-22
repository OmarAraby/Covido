from django.urls import path , include
from .views import forecast  , ChartData




app_name='forecast'

urlpatterns = [

    path('' ,  forecast, name='forecast'),
    path('api', ChartData.as_view(), name='api_data'),
 

]