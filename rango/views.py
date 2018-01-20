from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Cruchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'> About </a>")

def about(request):
    return HttpResponse("Rango says here is the about page! <br/> <a href='/rango/'> Index </a>")

