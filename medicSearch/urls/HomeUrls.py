from django.urls import path
from medicSearch.views import home_view

urlpatterns = [
    path('', home_view)
]