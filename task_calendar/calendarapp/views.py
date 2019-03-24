from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import DateInstance
from datetime import datetime
from .functions import last_day_of_month, generate_date_array

# Create your views here.
class IndexView(View):
    template_name = "calendarapp/index.html"

    def get(self,request):
        currdate = datetime.now()
        month = currdate.month
        year = currdate.year
        blocks = DateInstance.objects.filter(date__month = month, date__year = year)
        last_date = last_day_of_month(currdate.date())
        first_date = currdate.replace(day=1)
        date_array = generate_date_array(first_date,last_date)
        first_day = first_date.strftime("%A")
        return render(request, self.template_name,{'blocks':blocks, 'currdate':currdate, "date_array":date_array, "first_day":first_day})
