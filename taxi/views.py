from django.shortcuts import render
import json
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import redirect
from django.http import JsonResponse
from django.urls import reverse



# Create your views here.

def send_json(request):

    data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]

    return JsonResponse(data, safe=False)


def index(request):
    return HttpResponse("index page");


def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('username', 'taxivaxi')
    tutorial = request.COOKIES['username']
    print("cookies response")
    print(tutorial)
    return response

def getcookie(request):
    tutorial  = request.COOKIES['username']
    return HttpResponse("username: " + tutorial)

def testurl(request):
    data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]

    op_rates = JsonResponse(data, safe=False)
    #op_rates = 'test rate'
   # return reverse('redirectpath',rates=op_rates)
    question_id = 10
    return HttpResponseRedirect(reverse('redirectpath',args=(question_id,)))



def pathtoredirect(request,args):

    return HttpResponse("check redirect")



def carinfo(request):

    data = dict(name='maruti',
                model=[{'model_name': 'swift', 'price': '10000'}, {'model_name': 'alto', 'price': '50000'}])

    var1 = dict({'name':'maruti-suzuki','models':[{'name':'swift','price':'100000'},{'name':'alto','price':'200000'}],'indian':'yes'})

    pr1 = (var1['models'])

    #return HttpResponse(pr1)

    dump = json.dumps(var1)
    return HttpResponse(dump, content_type='application/json')