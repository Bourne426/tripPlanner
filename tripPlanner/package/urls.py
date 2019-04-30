from package import views
from django.urls import path
app_name= 'package'

urlpatterns = [
    path('query/', views.query_form_view, name='query_form'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hotels/', views.hotels, name='hotels'),
    path('packages/', views.packages, name='packages'),
    path('contact/', views.contact, name='contact'),
    path('custom/', views.customized_package_view, name='custom'),
    path('details/<pk>/', views.details_trip_package, name='details_trip_package'),
]
