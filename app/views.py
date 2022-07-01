from django.shortcuts import render
from django.http import request, response
from django.shortcuts import render, redirect
from .models import data

from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

option = 0
value = "" 

def home(request):

    optio = 0
    valu = ""

    if request.method == 'GET':
        optio = int(request.GET['option'])
        valu =  request.GET['input']    

    option = optio
    value = valu
    return render(request, 'app/index.html', {})




  
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format = None):
        print(option, value)
        labels = [
            'intensity',
            'likelihood', 
            'relevance', 
            'start_year', 
            'end_year', 
            'country', 
            'topic',
            'region',
            ]
        chartLabel = "my data"
        

        intensity_c = 0
        likelihood_c = 0
        relevance_c = 0
        start_year_c = 0
        end_year_c = 0
        country_c = 0
        topic_c = 0
        region_c = 0

        detail = {}

        if option == 1:
            if len(value) != 0:
                detail = data.objects.filter(end_year = int(value))
            
        elif option == 2:
            detail = data.objects.filter(topic = value)
        elif option == 3:
            detail = data.objects.filter(sector = value)
        elif option == 4:
            detail = data.objects.filter(region = value)
        elif option == 5:
            detail = data.objects.filter(pestle = value)
        elif option == 6:
            detail = data.objects.filter(source = value)
        elif option == 7:
            detail = data.objects.filter(country = value)
        

        for d in detail:
            intensity_c += d['intensity']
            likelihood_c += d['likelihood']
            relevance_c += d['relevance']
            start_year_c += d['start_year']
            end_year_c += d['end_year']
            country_c += d['country']
            topic_c += d['topic']
            region_c += d['region']

        chartdata = [intensity_c, likelihood_c, relevance_c, start_year_c, end_year_c, country_c, topic_c, region_c]

        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)