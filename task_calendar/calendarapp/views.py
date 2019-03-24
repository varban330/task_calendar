from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import DateInstance
from datetime import datetime
from .functions import last_day_of_month, generate_date_array, generate_sat_date_array,isttime
from .forms import DateForm

# Create your views here.
class IndexView(View):
    form_class = DateForm
    template_name = "calendarapp/index.html"

    def get(self,request):
        form = self.form_class(None)
        currdate = datetime.now()
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
        form = self.form_class(request.POST)
        month = request.POST["month"]
        year = request.POST["year"]
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
