#mysite\mysite\views.py

from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import json, requests
from pprint import pprint

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):

    url1 = 'http://intranet.defond.com/FarmControl/api/farmdata/getlastdevstatusdata/100/3/2/3/3/1'
    resp = requests.get(url= url1)
    data_set = resp.json()
    print('type of data_set = ' + str(type(data_set)))
    b=[]
    print('type of b = ' + str(type(b)))
    b +=[data_set]
    print('length of b = ' + str(len(b)))

    dev_id = str(b[0]['DevID'])
    dev_value = str (b[0]['Value'])
    log_time = str (b[0]['LogTime'])

    print('the value of DevID = '+ str(b[0]['DevID']))
    print('the value of Value = ' + str(b[0]['Value']))


    pprint(data_set)



    now = datetime.datetime.now()


    return render(request, 'current_datetime.html', {'current_date': now, 'dev_id': dev_id, 'dev_value': dev_value, 'log_time': log_time })
