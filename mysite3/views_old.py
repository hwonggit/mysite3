from django.http import HttpResponse
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

    print('the value of DevID = '+ str(b[0]['DevID']))
    print('the value of Value = ' + str(b[0]['Value']))


    pprint(data_set)

    now = datetime.datetime.now()
    html = "<html><body>the value of DevID =  %s</body></html>" % dev_id
    return HttpResponse(html)
