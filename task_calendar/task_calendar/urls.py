from django.contrib import admin
from django.urls import path
from calendarapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^update/', views.UpdateView.as_view(), name="update"),
    url(r'^add_task/', views.AddTask.as_view(), name="add-task"),
    url(r'^delete/', views.DeleteTask.as_view(), name="delete-task"),
    url(r'^test/', views.TestView.as_view(), name="test"),
]
