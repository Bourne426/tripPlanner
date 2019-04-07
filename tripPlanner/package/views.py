from django.shortcuts import render

from package.models import *
from .forms import Query_Form

# Create your views here.

def query_form_view(request):
    if request.method == 'POST':
        forms = Query_Form(request.POST)
        if forms.is_valid():
            destination=forms.cleaned_data['destination']
            # cityId = City.objects.raw('SELECT id from package_city WHERE Name=%s OR State=%s',[destination],[destination])
            # Pid = Trip_Package.objects.raw('SELECT id from package_trip_package_Cities WHERE city=%s',[cityId])

            P_list = Package_Details.objects.get(Package_Id=Pid)

            forms = {
                'message': "Your Query has been registered",
            }
            return render(request, 'package/Query_Submit.html', forms)
    else:
        forms = Query_Form()
    return render(request, 'package/Query_Form.html', {'forms': forms})
