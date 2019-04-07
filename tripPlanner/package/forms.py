from django import forms

class Query_Form(forms.Form):

    CITY_CHOICES = [
        ('1','Raipur'),
        ('2','Jodhpur'),
        ('3','Jaipur'),
        ('4','Jaisalmer'),
        ('5','Patna'),
        ('6','Bodh_Gaya'),
        ('7','Rajgir'),
        ('8','Kakolat'),
        ('9','Chennai'),
        ('10','Mahabalipuram'),
        ('11','Velacherry'),
        ('12','Sricity'),
        ('13','Vishakhapatnam'),
        ('14','Tirupati'),
        ('15','Ooty'),
        ('16','Bangalore'),
        ('17','Panji'),
        ('18','Lucknow'),
        ('19','Varanasi'),
        ('20','Allahabaad'),
        ('21','Ghaziabaad'),
        ('22','Jammu_Tawi'),
        ('23','Srinagar'),
        ('24','Leh'),
        ('25','Ladakh'),
        ('26','Chandigarh'),
        ('27','Mumbai'),
        ('28','New_delhi'),
        ('29','Kolkata'),
        ('30','Pune')
    ]
    origin = forms.CharField(label='origin', widget=forms.Select(choices=CITY_CHOICES))
    destination = forms.CharField(label='destination', widget=forms.Select(choices=CITY_CHOICES))
    start_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget)
    End_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget)
