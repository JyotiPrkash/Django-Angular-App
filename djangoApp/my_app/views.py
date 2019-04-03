#  Developed by Jyoti Prakash Das, Full Stack Web Developer, 
# LinkedIn -> https://www.linkedin.com/in/jyoti-prakash-das-220706108/
from django.shortcuts import render
from django.views.generic import TemplateView
import json
import requests

from django.http import HttpResponse,JsonResponse
import datetime

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def getSampleData(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        chat_data = {"response":"hey.. I am from Django", "time":now}
        
        return JsonResponse(chat_data)

def getRandomQuotes(request):
    respData= {}
    context={}
    # try:
    req = requests.get('https://geek-jokes.sameerkumar.website/api')
    print(req.text)
    # except:
    # context = { 'response': 'Internal Server Error', 'error':'something went wrong!!'}
        # return JsonResponse(context)
    if req.status_code == 200:
        respData = json.loads(req.text)
        context = { 'response': respData , 'error':'no error'}
    else:
        context = { 'response': 'api failed to fetch data ', 'error':req.text}
    return JsonResponse(context)