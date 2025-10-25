from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Customer

# Create your views here.
def customers(request):
    mycustomers = Customer.objects.all()
    template = loader.get_template('all_customers.html')
    context = {
      'mycustomers': mycustomers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mycustomer = Customer.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
      'mycustomer': mycustomer,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    print ('main is called')
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
      'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))


def toast_de(request):
    
    return render(request, 'Toast.html')

def ingredient_de(request):
    
    return render(request, 'Ingredient.html')
