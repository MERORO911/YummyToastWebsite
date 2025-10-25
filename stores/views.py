from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template import loader
from .models import Store, Booking
from customers.models import Customer
from stores.forms import BookingForm
from datetime import date
from django.contrib.auth.decorators import login_required

def stores(request):
  stores = Store.objects.all()
  template = loader.get_template('all_stores.html')
  context = {
    'stores': stores,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  store = Store.objects.get(id=id)
  template = loader.get_template('store_details.html')
  context = {
    'store': store,
  }
  return HttpResponse(template.render(context, request))

@login_required
def booking(request, store_id):
    print('booking view is called')
    if request.user.is_authenticated:
        if request.method == 'GET':
            print('GET method to booking form')
            initial = {
                'store': store_id,
                'cus': request.user,
                'date': date.today(),
                'address': ''
            }
            booking_form = BookingForm(initial)
            context = {'booking_form': booking_form}
            return render(request, 'booking.html', context)
        elif request.method == "POST":
            print('POST method to booking form')
            print(f"request.POST: {request.POST}")
            try:
                customer = Customer.objects.get(cus=request.user)
            except Customer.DoesNotExist:
                print(f'{request.user} is not a customer')
                return render(request, 'booking_error.html', None)
            
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking = booking_form.save(commit=False)
                booking.user = customer

                booking.save()
                print('Booking successfully (saved)')
                result = '訂購完成'
            else:
                print('Booking fails (form is not valid)')
                result = '訂購失敗'
            context = {
                'booking_form': booking_form,
                'result': result,
                'customer': customer,
            }
            return render(request, 'booking_result.html', context)
        else:
            return HttpResponseBadRequest()

@login_required
def my_bookings(request):
    ''' to show my booking list '''
    try:
        customer = Customer.objects.get(cus=request.user)
        print(f'Customer found: {customer}')
    except Customer.DoesNotExist:
        print(f'The cus {request.user} is not a customer')
        return render(request, 'booking_error.html', None)


    bookings = Booking.objects.filter(cus=request.user)

    print(f'All bookings by {request.user}:')
    for b in bookings:
        print(b)

    context = {'customer': customer, 'bookings': bookings}
    return render(request, 'my_bookings.html', context)

def getCustomer(request):
    print (request.user)
    try:
        customer = Customer.objects.get(cus=request.user)
        print (customer)
        return customer
    except:
        print (f"The cus {request.user} is not a customer")
        return render(request, 'booking_error.html', None)
    

