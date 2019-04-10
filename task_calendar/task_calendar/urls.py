from django.contrib import admin
from django.urls import path
from calendarapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^calendar/', views.IndexView.as_view(), name="index"),
    url(r'^test/', views.TestView.as_view(), name="test"),
]
