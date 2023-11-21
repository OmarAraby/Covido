from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ForecastingModelInterfaceImp
import pandas as pd

# Create your views here.




def forecast(request):
    confirmed_file=pd.read_json('https://api.covid19api.com/country/egypt/status/confirmed/live')
    recovered_file=pd.read_json('https://api.covid19api.com/country/egypt/status/recovered/live')
    death_file=pd.read_json('https://api.covid19api.com/country/egypt/status/deaths/live')



    recovery_cases = ForecastingModelInterfaceImp(
    file_source=confirmed_file,
    name_of_model="recovery_cases")
    forecasting = recovery_cases.forecast()
    labels = forecasting['ds']
    chartLabel = "covid-19"
    chartdata = confirmed_file['Cases']
    recovered = recovered_file['Cases']
    death = death_file['Cases']
    forecast = forecasting['yhat']
    forecast_lower = forecasting['yhat_lower']
    forecast_upper = forecasting['yhat_upper']


 


    return render(request,'forecast.html')

