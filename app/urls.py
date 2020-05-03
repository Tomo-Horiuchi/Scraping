from django.contrib import admin
from django.urls import path, include
from .views import Account, Keyword, Time


urlpatterns = [
    path('account/', Account.as_view(), name='account'),
    path('keyword/', Keyword.as_view(), name='keyword'),
    path('time/', Time.as_view(), name='time'),
]
