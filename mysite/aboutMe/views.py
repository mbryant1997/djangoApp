from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    response = {
    "Name" : "Mekhi Bryant",

    "Track" : "Backend(Python)", 

    "Message" : "Hello mentor. It's defintely getting harder but I'm doing alright."
    }

    return JsonResponse(response)
    

