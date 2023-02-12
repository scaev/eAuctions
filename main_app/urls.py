from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('auctions/', views.auctions_index, name='index'),
    path('auctions/<int:auction_id>/', views.auctions_detail, name='detail'),
]