from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Homepage')

def contact(request):
    return HttpResponse('Contact')

def products(request):
    return HttpResponse('list product')

def product(request, product_id):
    result = 'you are looking at product %i' %product_id
    return HttpResponse(result)

def read_year(request, year):
    text = '<h3>The year is %s</h3>' %year
    return HttpResponse(text)

def index_2(request):
    hello = 'Welcome onboard'
    return render(request, 'firstapp/index.html', {'hi':hello})