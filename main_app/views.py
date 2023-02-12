import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Auction, User, Bid  

# Create your views here.



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def auctions_index(request):
  auctions = Auction.objects.all()
  return render(request, 'auctions/index.html', {
    'auctions': auctions
  })

def auctions_detail(request, auction_id):
  auction = Auction.objects.get(id=auction_id)
  return render(request, 'auctions/detail.html', {
    'auction': auction,
  })