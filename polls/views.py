from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests
import json
from polls.models import Question, Choice, UserStatus
from django.utils import timezone

def index(request):
    output = ""
    for p in UserStatus.objects.filter(user_id='U0E0DFN1Z'):
        output += (p.user_id) + "     "
        output += (p.status) + "     "
        output += str(p.status_date) + "||"
      
    return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index. status = " + str(r.status_code))
