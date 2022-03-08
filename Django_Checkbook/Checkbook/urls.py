from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('creat/', views.create_account, name='create'),
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction')
]