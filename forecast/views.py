from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .forecasting_interface_impl import ForecastingModelInterfaceImp
import pandas as pd

# Create your views here.3




url = "https://covid-19-tracking.p.rapidapi.com/v1/egypt"

headers = {
	"X-RapidAPI-Key": "3bf1f7dc73msh6c437be43ba2064p1ddbe8jsn4f6b3dd4ddf1",
	"X-RapidAPI-Host": "covid-19-tracking.p.rapidapi.com"
}
response = requests.get(url, headers=headers)


# Check if the request was successful before trying to parse JSON
if response.status_code == 200:
    data = response.json()

    chartLabel = "Covid-19"
    chartdata = [data['Total Cases_text']]
    recovered = [data['Total Recovered_text']]
    death = [data['Total Deaths_text']]
else:
    # Handle the case where the request was not successful
    chartLabel = "Covid-19"
    chartdata = []
    recovered = []
    death = []




class ForecastView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'forecast.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "chartLabel": chartLabel,
            "chartdata": chartdata,
            "recovered": recovered,
            "death": death,
        }
        return Response(data)

    









# recovered_file=pd.read_json('https://api.covid19api.com/country/egypt/status/recovered/live')
# death_file=pd.read_json('https://api.covid19api.com/country/egypt/status/deaths/live')


# recovered = recovered_file['Cases']
# death = death_file['Cases']
# forecast = forecasting['yhat']
# forecast_lower = forecasting['yhat_lower']
# forecast_upper = forecasting['yhat_upper']

#recovery_cases = ForecastingModelInterfaceImp(file_source=confirmed_file,name_of_model="recovery_cases")
#forecasting = recovery_cases.forecast()
#labels = forecasting['ds']


# class ForecastView(View):
#     def get(self, request, *args, **kwargs):
#         url = "https://covid-19-tracking.p.rapidapi.com/v1/egypt"
#         headers = {
#             "X-RapidAPI-Key": "3bf1f7dc73msh6c437be43ba2064p1ddbe8jsn4f6b3dd4ddf1",
#             "X-RapidAPI-Host": "covid-19-tracking.p.rapidapi.com"
#         }

#         response = requests.get(url, headers=headers)

#         # Check if the request was successful before trying to parse JSON
#         if response.status_code == 200:
#             data = response.json()
#         else:
#             # Handle the case where the request was not successful
#             data = {}

#         return render(request, 'forecast.html', {'data': data})


# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         chartLabel = "Covid-19"
#         chartdata = [request.data.get('Total Cases_text', 0)]
#         recovered = [request.data.get('Total Recovered_text', 0)]
#         death = [request.data.get('Total Deaths_text', 0)]

#         data = {
#             "chartLabel": chartLabel,
#             "chartdata": chartdata,
#             "recovered": recovered,
#             "death": death,
#         }
#         return Response(data)

