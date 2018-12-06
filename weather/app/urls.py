from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='weather'),
    path('pin/<city>', views.pin,name='pin'),
    path('unpin/<city>', views.unpin,name='unpin'),
]