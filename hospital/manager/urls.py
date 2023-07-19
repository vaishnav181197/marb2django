from django.urls import path
from .views import *

urlpatterns=[
    path('doc',AddDocView.as_view(),name="doc"),
    path('pat',AddPateintView.as_view(),name="pat"),
]