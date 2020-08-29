from django.contrib import admin
from django.urls import path,include
from prediction import views
from django.views.generic.base import RedirectView

urlpatterns = [        
path('',RedirectView.as_view(url='predict/')),
path('predict/', views.predict,name='predict'),
]