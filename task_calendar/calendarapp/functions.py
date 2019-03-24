import datetime

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
