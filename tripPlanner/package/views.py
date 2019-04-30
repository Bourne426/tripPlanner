from django.db.models import Q
from django.shortcuts import render
from django.db import connection

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
            destination = destination.title()
            print("printing destination")
            print(destination)
            # city_id = City.objects.filter(Q(Name__startswith=destination))
            #city_id1 = City.objects.raw("SELECT * FROM package_city WHERE lower(Name) = %s",[destination])[0].id
            # print(city_id)
            #print(city_id1)
            package=[]
            with connection.cursor() as cursor:
                query = 'SELECT * FROM package_city WHERE lower(Name) LIKE lower(\"%s' %destination +'%'+'\")'
                print(query)
                cursor.execute(query)
                city_id = cursor.fetchone()
                if not city_id:
                    photo = Gallery.objects.get(Activity_Id=3)
                    print(photo)
                    forms = Query_Form()
                    return render(request, 'index.html',{'forms':forms,'photo':photo,})
                print(city_id)
                cursor.execute("SELECT * FROM package_trip_package_Cities WHERE city_id = %s",[city_id[0]])
                raw = cursor.fetchall()
                for i in raw:
                    pkg =Trip_Package.objects.raw("SELECT * FROM package_trip_package WHERE id = %s",[i[1]])
                    package.append(pkg[0])
                    for city in pkg[0].Cities.all():
                        print(city.Name)
            # for cid in city_id1:
            #     print(cid)
            #     Trip_Package.objects.raw("SELECT * FROM SELECT id FROM package_city WHERE id= cid")
            # city_id = City.objects.get(pk=city_id)
            # packages=[]
            #print(len(city_id))
            # for i in range(len(city_id)):
            print(package)
            # packages = Trip_Package.objects.filter(Cities__in=city_id)
            # print(Trip_Package.objects.raw("SELECT * FROM package_trip_package_Cities WHERE city_id = %s",[city_id1]))
            #
            # print("printing packages")
            # print(packages)
            context = {
                'packages': package,

                # 'city_id': city_id,
            }

            print(context)
            return render(request, 'packages.html', context)
    else:
        photo = Gallery.objects.get(Activity_Id=3)
        print(photo)
        forms = Query_Form()
        return render(request, 'index.html',{'forms':forms,'photo':photo,})

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
