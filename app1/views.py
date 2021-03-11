from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def madhan(request):
    return HttpResponse('hai this is madan')



def bye(request):
    return render(request,'app1/bye.html')