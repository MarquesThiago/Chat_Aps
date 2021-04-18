from django.shortcuts import render
from django.http import (HttpResponse, JsonResponse, HttpResponseBadRequest, 
    HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError) 
from django.views.decorators.csrf import csrf_exempt
from json import  loads
from .models import *


# function multi-used 
def req_decode(request):
    json_text = request.body.decode("utf-8")
    return loads(json_text)

# home
# virifed user 
# locahost/
@csrf_exempt
def index(request):
    body = req_decode(request = request)
    mail = body["email"]
    password = body["password"]
    if password not in (None, "", " ") or mail not in (None, "", " "):
        
        user = valit_user(password= password, mail= mail)
        
        if "error" not in  user.keys():
            return JsonResponse(user)
        else:
            return HttpResponseNotFound("ERROR: 404 - Not Found User in Server")
    
    else:
        return HttpResponseBadRequest("ERROR: 400 - Don't insered user valild")

# information of user 
# localhost/userInfo
@csrf_exempt
def user(request):
    body = req_decode(request = request)
    user = body["id_user"]
    if user in (None, ""):
        return HttpResponseBadRequest("ERROR: 400 - Don't insered user valild")    
    else:
        info = info_user(id_user= user)
        if "error" not in info.keys():
            return JsonResponse(info)
        else: 
            return HttpResponseNotFound("ERROR: 404 - Not Found User in Server")

#search group or people 
#localhost/search
@csrf_exempt
def seach_group(request):
    body = req_decode(request= request)
    user = body["names"]
    test = body["test"]
    if user in (None, ""):
        return HttpResponseBadRequest("ERROR: 400 - Don't insered user valild")
    elif user not in (None, "") and test not in ("True", "true", True):
        return HttpResponseNotFound("ERROR: 404 - Not Found User in Server")
    else:
        return JsonResponse({ 
            "status": "true", 
            "users" : 
            "[{name: manoel siqueira Averlar, id_group: 123456879 }, {name: Franscisoc almeida, id_group: 123456789}]"
        })

# last people or group user talk
# localhost/cache
@csrf_exempt
def cache_user(request):
    body = req_decode(request = request)
    user = body["id_user"]
    test = body["test"]
    if user in (None, ""):
        return HttpResponseBadRequest("ERROR: 400 - Don't insered user valild")
    elif user not in (None, "") and test not in ("True", "true", True):
        return HttpResponseNotFound("ERROR: 404 - Not Found User in Server")
    else:
        return JsonResponse({
          "user" : """ [ {'name': 'Luis Herique',
            'Cargo': 'Analista Field Service Pleno',
            'Dept': 'Tecnologia da Informação',
            'Email': 'LuizHerinque@verdinhooverde.com.br',
            'phone': '(55) 11 987456898'} , 
            {'name': 'Manoel Sousa',
            'Cargo': 'Analista Flutuaçao Pleno',
            'Dept': 'CRM',
            'Email': 'manoelsousa@verdinhooverde.com.br',
            'phone': '(55) 11 987456898'} ]"""})

#return messages
# localhost/message
@csrf_exempt
def message(request):
    body = req_decode(request = request)
    return JsonResponse({"response" : "{user: 'Leonardo', 'message' : 'você é um babaca' }"})