from django.db import models
from datetime import datetime

class DateInstance(models.Model):
    status = models.CharField(max_length = 7, default='None')
    task1 = models.CharField(max_length = 17, default='None')
    task2 = models.CharField(max_length = 17, default='None')
    task3 = models.CharField(max_length = 17, default='None')
    date = models.DateField(default=datetime.now)

    def __str__(self):
        string = self.date.strftime("%d/%m/%Y") + ' -- ' + self.status
        return string
