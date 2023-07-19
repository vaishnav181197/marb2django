from django.urls import path 
from .views import *

urlpatterns=[
    path('fst',first),
    path('sec',second),
    path('test',testview),
    path('log',log,name="lg"),
    path('add',add,name="ad"),
    path('addc',AddView.as_view()),
    path('word',WordView.as_view()),
]