from django.urls import path , include
from .views import ForecastView  , ChartData




app_name='forecast'

urlpatterns = [

    path('' ,  ForecastView.as_view(), name='forecast'),
    path('api', ChartData.as_view(), name='api_data'),
 

]