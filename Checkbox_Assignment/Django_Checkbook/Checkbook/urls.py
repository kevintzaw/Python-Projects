from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('creative/', views.create_account, name='create'),
    path('balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction')
]