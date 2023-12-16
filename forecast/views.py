from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .forecasting_interface_impl import ForecastingModelInterfaceImp
import pandas as pd

# Create your views here.3




url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    "X-RapidAPI-Key": "************************************",
    "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

# Check if the request was successful before trying to parse JSON
if response.status_code == 200:
    data = response.json()

    # Extract data for Portugal
    egypt_data = next((item for item in data['countries_stat'] if item['country_name'] == 'Egypt'), None)
    
    if egypt_data:
        chartLabel = [egypt_data['country_name']]
        chartdata = [egypt_data['cases']]
        recovered = [egypt_data['total_recovered']]
        death = [egypt_data['deaths']]
    else:
        # Handle the case where Portugal data is not found
        chartLabel = ["Covid-19"]
        chartdata = []
        recovered = []
        death = []
else:
    # Handle the case where the request was not successful
    chartLabel = ["Covid-19"]
    chartdata = []
    recovered = []
    death = []

def forecast(request):
    # url = "https://covid-19-tracking.p.rapidapi.com/v1/egypt"
    # headers = {
    #     "X-RapidAPI-Key": "3bf1f7dc73msh6c437be43ba2064p1ddbe8jsn4f6b3dd4ddf1",
    #     "X-RapidAPI-Host": "covid-19-tracking.p.rapidapi.com"
    # }
    url = 'http://127.0.0.1:8000/forecast/api'

    response = requests.get(url)
    data = response.json()


    chartLabel = "Covid-19"
    total_cases = int(data['chartdata'][0].replace(',', ''))
    recovered = int(data['recovered'][0].replace(',', ''))
    death = int(data['death'][0].replace(',', ''))
    all_inf = [total_cases , recovered, death]

    context = {
        'chartLabel': chartLabel,
        'total_cases': total_cases,
        'recovered': recovered,
        'death': death,
        'all_inf':all_inf
    }

    return render(request, 'forecast.html',context)








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

