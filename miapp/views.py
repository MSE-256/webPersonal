from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def HelloWorld(request):
    return HttpResponse("HELLO WORLD")

class HelloBahamas(View):
    def get(self, request):
        return HttpResponse('Hello Bahamas')