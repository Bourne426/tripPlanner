from django.db.models import Q
from django.shortcuts import render

from package.models import *

# from tripPlanner.package.models import Package_Details
from .forms import Query_Form

# Create your views here.

def query_form_view(request):
    if request.method == 'POST':
        forms = Query_Form(request.POST)


        print("printing forms")
        print(forms)
        if forms.is_valid():
            print("hh")
            destination = forms.cleaned_data['destination']
            print("printing destination")
            print(destination)

            city_id = City.objects.filter(Q(Name__startswith=destination))
            print(city_id)
            # city_id = City.objects.get(pk=city_id)
            # packages=[]
            # print(len(city_id))
            # for i in range(len(city_id)):
            packages = Trip_Package.objects.filter(Cities__in=city_id)

            print("printing packages")
            print(packages)
            context = {
                'packages': packages,
                # 'city_id': city_id,
            }
            return render(request, 'packages.html', context)
    else:
        forms = Query_Form()
        context = {
            'forms': forms,
        }
        return render(request, 'index.html', context)

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