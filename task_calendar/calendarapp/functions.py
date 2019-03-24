import datetime
from pytz import timezone

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)

def generate_date_array(start,end):
    date_array = list()
    step = datetime.timedelta(days=1)
    while start.date()<=end:
        date_array.append(start.date())
        start += step
    return date_array

def generate_sat_date_array(date_array):
    sat_date_array = list()
    for date in date_array:
        d = datetime.datetime(date.year, date.month, date.day)
        if d.strftime("%A") == 'Saturday':
            sat_date_array.append(date)
    return sat_date_array

def isttime(date_utc):
    date_asia = date_utc.astimezone(timezone('Asia/Kolkata'))
    return date_asia
