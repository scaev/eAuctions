from django.shortcuts import render
from .models import Auction, User, Bid  

# Create your views here.



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def auctions_index(request):
  auctions = Auction.objects.all()
  return render(request, 'cats/index.html', {
    'auctions': auctions
  })