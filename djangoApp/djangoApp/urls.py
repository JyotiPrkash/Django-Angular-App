#  Developed by Jyoti Prakash Das, Full Stack Web Developer, 
# LinkedIn -> https://www.linkedin.com/in/jyoti-prakash-das-220706108/


from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from my_app import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('getSampleData/', views.getSampleData, name='getSampleData'),
	path('getRandomQuotes/', views.getRandomQuotes, name='getRandomQuotes')
]