from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    flights = []
    if request.method == 'GET' and request.GET.get('source'):
        source = request.GET.get('source')
        destination = request.GET.get('destination')
        date = request.GET.get('departure')
        print(date)

        flights = Flight.objects.filter(
            source__iexact = source,
            destination__iexact = destination,
            departure__date = date
        )
        print(flights)
    return render(request,'home.html',{'flights':flights})