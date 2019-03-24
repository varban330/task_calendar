from django.contrib import admin
from django.urls import path
from calendarapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', views.IndexView.as_view(), name="index"),
    url(r'^update/', views.UpdateView.as_view(), name="update"),
]
