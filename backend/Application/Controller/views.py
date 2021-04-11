from django.shortcuts import render
from django.http import (HttpResponse, JsonResponse) 
from django.views.decorators.csrf import csrf_exempt
from json import  loads

def req_decode(request):
    json_text = request.body.decode("utf-8")
    return loads(json_text)

@csrf_exempt
def index(request):
    body = req_decode(request = request)
    if body['test'] in ( "true", "True", True):
        return JsonResponse({
            "verify":"True", 
            "id_user" : "12345687932", 
            })
    else:

        return JsonResponse({"verify" : "False"})

@csrf_exempt
def user(request):
    body = req_decode(request = request)
    user = body["id_user"]
    test = body["test"]
    if user in (None, ""):
        return HttpResponse("Don't insered id_user valild")
    elif user not in (None, "") and test in ("False", "false", False):
        return HttpResponse("Don't Found User")
    else:
        return JsonResponse({
            "name": "Luis Herique",
            "Cargo": "Analista Field Service Pleno",
            "Dept": "Tecnologia da Informação",
            "Email": "LuizHerinque@verdinhooverde.com.br",
            "phone": "(55) 11 987456898"})

@csrf_exempt
def seach_group(request):
    body = req_decode(request= request)
    user = body["names"]
    test = body["test"]
    if user in (None, ""):
        return HttpResponse("Don't insered name valild")
    elif user not in (None, "") and test in ("False", "false", False):
            return HttpResponse("Don't Found User")
    else:
        return JsonResponse({ "users" : 
            "[{name: manoel siqueira Averlar, id_group: 123456879 }, {name: Franscisoc almeida, id_group: 123456789}]"
        })

@csrf_exempt
def cache_user(request):
    body = req_decode(request = request)
    user = body["id_user"]
    test = body["test"]
    if user in (None, ""):
        return HttpResponse("Don't insered id_user valild")
    elif user not in (None, "") and test in ("False", "false", False):
        return HttpResponse("Don't Found User")
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

@csrf_exempt
def message(request):
    body = req_decode(request = request)
    return JsonResponse({"response" : "{user: 'Leonardo', 'message' : 'você é um babaca' }"})