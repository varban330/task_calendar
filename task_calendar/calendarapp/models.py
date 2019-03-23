from django.db import models

class DateModel(models.Model):
    status = models.CharField(max_length = 7)
    task = models.CharField(max_length = 17)
    date = models.DateField()

    def __str__(self):
        string = self.date.strftime('%d/%m/%Y') + ' -- ' + self.status + ' -- ' + self.task
        return string
