from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bhupal(request):
    return HttpResponse('hai this is bhupal')


def hai(request):
    return render(request,'app2/hai.html')