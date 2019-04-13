from django import forms
from .models import City
class Query_Form(forms.Form):
    #
    # choice = City.objects.all()
    # choice = list(choice) #converting it to queryset into string
    # choice2 = []
    # for x in choice:
    #     x = str(x)
    #     city_tuple_value = (x, x) #here (x,x) is like key value pair i.e (x = returned value after form submission, x = city name)
    #     choice2.append(city_tuple_value)
    #
    destination = forms.CharField(label='Destination')
    # travel_date = forms.DateField(label='Travel Date', widget=forms.SelectDateWidget)
