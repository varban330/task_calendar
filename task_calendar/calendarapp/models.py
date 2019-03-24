from django.db import models

class DateBlock(models.Model):
    status = models.CharField(max_length = 7)
    task1 = models.CharField(max_length = 17)
    task2 = models.CharField(max_length = 17)
    task3 = models.CharField(max_length = 17)
    date = models.DateField()

    def __str__(self):
        string = self.date.strftime('%d/%m/%Y') + ' -- ' + self.status
        return string
