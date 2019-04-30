from package import views
from django.urls import path
app_name= 'package'

urlpatterns = [
    path('index/', views.query_form_view, name='index'),
    # path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hotels/', views.hotels, name='hotels'),
    path('packages/', views.packages, name='packages'),
    path('custom/', views.Coustomize_view, name='custom'),
    path('details/<pk>/', views.details_trip_package, name='details_trip_package'),
]
