import uuid
import boto3
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Auction, User, Bid, Photo  
from .forms import BiddingForm

# Create your views here.

def add_photo(request, auction_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3= boto3.client("s3")
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind("."):]

    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)

      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"

      Photo.objects.create(url=url, auction_id = auction_id)

    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  
  return redirect('detail', auction_id = auction_id)


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
  bids = auction.bid_set.all()
  return render(request, 'auctions/detail.html', {
    'auction': auction,'bids': bids
  })

def add_bid(request, auction_id):
  form = BiddingForm(request.POST)
  if form.is_valid():
    new_bid = form.save(commit = False)
    new_bid.auction_id = auction_id
    new_bid.save()
  return redirect('detail', auction_id = auction_id)  
  

