from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('reg/',views.reg , name='reg'),
    path('main/',views.main , name='main'),
    path('logout/',views.logout , name='logout'),
    path('chat/<id>',views.chat , name = 'chat' ),
]