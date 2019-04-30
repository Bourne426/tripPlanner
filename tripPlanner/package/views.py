from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from package.models import *

# from tripPlanner.package.models import Package_Details
from package.models import Package_Details
from .forms import Query_Form

# Create your views here.

def query_form_view(request):
    if request.method == 'POST':
        forms = Query_Form(request.POST)
        if forms.is_valid():
            destination = forms.cleaned_data['destination']
            city_id = City.objects.filter(Q(Name__startswith=destination))
            packages = Trip_Package.objects.filter(Cities__in=city_id)
            context = {
                'packages': packages,
            }
            return render(request, 'packages.html', context)
    else:
        forms = Query_Form()
        context = {
            'forms': forms,
        }
        return render(request, 'index.html', context)

def details_trip_package(request,pk):
    package = Trip_Package.objects.filter(pk=pk)
    package_details = Package_Details.objects.filter(Package_Id__in=package)
    city=package_details.values('City')
    city_list = [dict(q) for q in city]
    city_id = []
    for i in range(len(city_list)):
        id_city=city_list[i]["City"]
        id_city=str(id_city)
        city_id.append(id_city)
    city = City.objects.filter(pk__in=city_id)
    Activity = Total_Activities.objects.filter(City_Id__in=city)
    context = {
        'package_details': package_details,
        'city': city,
        'Activity': Activity,
    }
    return render(request, 'package/packagedetails.html', context)

@login_required
def book_package(request,booking_id):
    if request.method == 'POST':
        forms = Booking_Form(request.POST, request.FILES)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.User_Id = request.user
            instance.save()

    else:
        forms = Booking_Form()
        context = {
            'forms': forms
        }
        return render(request, 'package/bookings.html', context)

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def hotels(request):
    return render(request,'hotels.html')


def packages(request):
    return render(request,'packages.html')


def contact(request):
    return render(request,'contact.html')


def customized_package_view(request):
    if request.method == 'POST':
        forms = Customized_Package_Form(request.POST)
        if forms.is_valid():
            activities = forms.cleaned_data['Activities']
            print(activities)
            context = {
                'forms':forms,
            }
            return HttpResponse("ALRIGHT")

    else:
        forms = Customized_Package_Form()
        context={
            'forms': forms,
        }
        return render(request,'package/booking.html', context)
