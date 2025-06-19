#from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', name='expenses', view=views.ExpenseListView.as_view()),
]
