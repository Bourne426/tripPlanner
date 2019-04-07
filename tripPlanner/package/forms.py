from django import forms
from .models import City
class Query_Form(forms.Form):

    choice = City.objects.all()
    # choice = [dict(q) for q in choice]

    choice = list(choice)
    # print(type(choice))
    i = 0
    choice2 = []
    for x in choice:
        # print(x)
        x = str(x)
        # print(type(x))
        c1 = (i, x)
        # print(c1)
        choice2.append(c1)
        i = i + 1
    print(choice2)

    origin = forms.CharField(label='origin', widget=forms.Select(choices=choice2))
    destination = forms.CharField(label='destination', widget=forms.Select(choices=choice2))
    start_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget)
    End_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget)
