from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .models import DateInstance
from datetime import datetime
from .functions import last_day_of_month, generate_date_array, generate_sat_date_array,isttime
from .forms import DateForm
from rest_framework.views import APIView
import json
from django.urls import reverse

# Create your views here.
class IndexView(View):
    form_class = DateForm
    template_name = "calendarapp/index.html"

    def get(self,request):
        form = self.form_class(request.GET)
        if not request.GET.keys():
            currdate = datetime.now()
        else:
            month = request.GET["month"]
            year = request.GET["year"]
            currdate = datetime(int(year),int(month),10)
        currdate = isttime(currdate)
        month = currdate.month
        year = currdate.year
        blocks = DateInstance.objects.filter(date__month = month, date__year = year)
        last_date = last_day_of_month(currdate.date())
        first_date = currdate.replace(day=1)
        date_array = generate_date_array(first_date,last_date)
        first_day = first_date.strftime("%A")
        date_array = date_array[1:]
        sat_date_array = generate_sat_date_array(date_array)
        block_date_array = list()
        for block in blocks:
            block_date_array.append(block.date)
        return render(request, self.template_name,{'form':form, 'blocks':blocks, 'currdate':currdate, "date_array":date_array, "sat_date_array":sat_date_array, "block_date_array":block_date_array ,"first_day":first_day, "first_date":first_date.date()})

    def post(self,request):
        form = self.form_class(request.GET)
        print(request.POST)
        date_req = request.POST['date']
        print(date_req)
        date_time = datetime.strptime(date_req,"%d/%m/%Y")
        date = date_time.date()
        status = request.POST['status']
        task1 = request.POST['task1']
        task2 = request.POST['task2']
        task3 = request.POST['task3']
        blocks  = DateInstance.objects.filter(date = date)
        if blocks:
            block = blocks[0]
            block.status = status
            block.task1 = task1
            block.task2 = task2
            block.task3 = task3
            block.save()
        else:
            block = DateInstance()
            block.status = status
            block.task1 = task1
            block.task2 = task2
            block.task3 = task3
            block.date = date
            block.save()
        if not request.GET.keys():
            currdate = datetime.now()
        else:
            month = request.GET["month"]
            year = request.GET["year"]
            currdate = datetime(int(year),int(month),10)
        currdate = isttime(currdate)
        month = currdate.month
        year = currdate.year
        blocks = DateInstance.objects.filter(date__month = month, date__year = year)
        last_date = last_day_of_month(currdate.date())
        first_date = currdate.replace(day=1)
        date_array = generate_date_array(first_date,last_date)
        first_day = first_date.strftime("%A")
        date_array = date_array[1:]
        sat_date_array = generate_sat_date_array(date_array)
        block_date_array = list()
        for block in blocks:
            block_date_array.append(block.date)
        return render(request, self.template_name,{'form':form, 'blocks':blocks, 'currdate':currdate, "date_array":date_array, "sat_date_array":sat_date_array, "block_date_array":block_date_array ,"first_day":first_day, "first_date":first_date.date()})

class TestView(APIView):
    def get(self, request):
            dict = {'message': 'Hi,This is your developer, Varun this side'}
            return HttpResponse(json.dumps(dict),status=200)

    def post(self,request):
            dict = {'message': 'Hi,This is your developer, Varun this side'}
            return HttpResponse(json.dumps(dict), status=200)
