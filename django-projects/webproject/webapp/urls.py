from . import views
from django.urls import path

urlpatterns = [
    path('home1', views.homepage, name='homepage'),
    path('update', views.updatedata, name='update data'),
    path('register', views.register, name='register'),
    path('submit', views.acknowledge, name='acknowledge'),
]
