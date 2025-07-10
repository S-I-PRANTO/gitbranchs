# from django.shortcuts import render
from django.http import HttpResponse;

def home (request):
    return HttpResponse("This is Home site ")

def id_show (request,id):
    return HttpResponse(f"This is id is {id} ")

def test_other (request):
    return HttpResponse("This is Other_site ")

