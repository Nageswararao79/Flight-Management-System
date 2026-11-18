from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from flights.models import Flight
# Create your views here.
@login_required(login_url='login')
def book_flight(request,flight_id):
    flight = get_object_or_404(Flight, id = flight_id)
    if request.method == 'POST':
        a = request.POST['pname']
        b = request.POST['snum']

        Booking.objects.create(
            user = request.user,
            flight = flight ,
            passenger_name = a ,
            seat_number = b
        )
        return redirect('mybookings')
    return render(request,'booking.html',{'data':flight})

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request,'mybook.html',{'data':bookings})