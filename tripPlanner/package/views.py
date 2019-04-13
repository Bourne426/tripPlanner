from django.shortcuts import render

from package.models import *

# from tripPlanner.package.models import Package_Details
from .forms import Query_Form

# Create your views here.

def query_form_view(request):
    if request.method == 'POST':
        forms = Query_Form(request.POST)
        if forms.is_valid():
            destination = forms.cleaned_data['destination']
            city_id = City.objects.get(Name=destination)
            packages = Trip_Package.objects.filter(Cities=city_id)
            print("printing packages")
            print(packages)
            context = {
                'packages': packages,
            }
            return render(request, 'package/Query_Submit.html', context)
    else:
        forms = Query_Form()
    return render(request, 'package/Query_Form.html', {'forms': forms})
