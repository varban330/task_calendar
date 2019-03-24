from django.contrib import admin
from django.urls import path
from calendarapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^calendar/', views.IndexView.as_view(), name="index"),
    url(r'^update/', views.UpdateView.as_view(), name="update"),
    url(r'^record/', views.RecordView.as_view(), name="record"),
    url(r'^test/', views.TestView.as_view(), name="test"),
]
