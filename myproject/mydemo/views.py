from django.shortcuts import render

from django.http import HttpResponse

def mydemo(request):
    return HttpResponse("Hello,World. You're at the polls index.")

