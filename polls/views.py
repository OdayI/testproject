from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests
import json
from polls.models import Question, Choice
from django.utils import timezone

def index(request):
    r = requests.get('https://private-86ccf-users169.apiary-mock.com/list')
    q = Question(question_text="What's new?", pub_date=timezone.now())
    q.save()
    dtaReturned = r.json()
    output = ""
    for jo in dtaReturned["members"]: 
        output = output + jo["id"] + "\n"
        output = jo["id"]
      
    return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index. status = " + str(r.status_code))
