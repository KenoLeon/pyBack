from pyBack import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.serveData, name='data'),
]
