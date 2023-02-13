import uuid
import boto3
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Auction, User, Bid, Photo  
from .forms import BiddingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class AuctionCreate(LoginRequiredMixin, CreateView):
  model = Auction
  fields = ['title', 'description', 'starting_price', 'end_date' ]

  def form_valid(self, form):
    form.instance.user = self.requests.user
    return super().form_valid(form)

class AuctionUpdate(LoginRequiredMixin, UpdateView):
  model = Auction
  fields = ['title', 'description', 'starting_price', 'end_date']

class AuctionDelete(LoginRequiredMixin, DeleteView):
  model = Auction
  success_url = '/auctions'


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
  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

