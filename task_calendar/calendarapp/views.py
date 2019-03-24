from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import DateBlock
from datetime import datetime

# Create your views here.
class IndexView(View):
    template_name = "calendarapp/index.html"

    def get(self,request):
        currdate = datetime.now()
        month = currdate.month
        year = currdate.year
        blocks = DateBlock.objects.filter(date.month == month and date.year == year)
        return render(request, self.template_name)
