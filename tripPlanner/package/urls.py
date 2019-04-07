from package import views
from django.urls import path
app_name= 'package'

urlpatterns = [
    path('query/', views.query_form_view, name='query_form'),
]
