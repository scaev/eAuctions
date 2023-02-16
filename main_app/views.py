import uuid
import boto3
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Auction, User, Bid, Photo
from .forms import BiddingForm
from datetime import date, datetime
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect





# Create your views here.

class AuctionCreate(LoginRequiredMixin, CreateView):
  model = Auction
  fields = ['title', 'description', 'starting_price', 'end_date', 'condition', 'category' ]

  def form_valid(self, form):
    form.instance.user = self.request.user
    response = super().form_valid(form)
    Bid.objects.create(amount = form.instance.starting_price, user = self.request.user, auction = self.object)
    return response


class AuctionUpdate(LoginRequiredMixin, UpdateView):
  model = Auction
  fields = ['title', 'description', 'starting_price', 'end_date']

class AuctionDelete(LoginRequiredMixin, DeleteView):
  model = Auction
  success_url = '/auctions'

@login_required
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
  bid_form = BiddingForm()
  current_auction = Auction.objects.get(id=auction_id)
  bids_current_auction = current_auction.bid_set.all()
  max_bid = bids_current_auction.order_by('-amount')[:1]
  max_bid_amount = max_bid.first().amount
  condition = Auction.objects.filter(condition="used")
  category = Auction.objects.filter(category="others")
  return render(request, 'auctions/detail.html', {
    'auction': auction,'bids': bids, 'bid_form' : bid_form, 'max_bid_amount':max_bid_amount, 'condition':condition, 'category':category,
  })


@login_required
def add_bid(request, auction_id):
  form = BiddingForm(request.POST)
  if form.is_valid():
    new_bid = form.save(commit = False)
    new_bid.auction_id = auction_id
    new_bid.user_id= request.user.id
    current_auction = Auction.objects.get(id=auction_id)
    bids_current_auction = current_auction.bid_set.all()
    max_bid = bids_current_auction.order_by('-amount')[:1]
    max_bid_amount = max_bid.first().amount
    if max_bid_amount < new_bid.amount:
      new_bid.save()
    else:
      error_message = 'Please place a bigger amount - try again'
  return redirect('detail', auction_id = auction_id,)  
  

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


# def signup(request):
#   print("I ran")
#   error_message = ''
#   form = None
#   if request.method == 'POST':
#     # This is how to create a 'user' form object
#     # that includes the data from the browser
#     form = UserCreationForm(request.POST)
#     print("String")
#     if form.is_valid():
#       try: 
#        # This will add the user to the database
#         user = form.save()
#         print(user)
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         # This is how we log a user in via code
#         login(request, user)
#         return redirect('index')
#       except Exception as e: 
#         print(e)
#         return redirect("index")

#     else:
#       error_message = 'Invalid sign up - try again'
#       form = UserCreationForm()
#       print(form.errors)
#       return HttpResponseRedirect("/")
      
#   # A bad POST or a GET request, so render signup.html with an empty form
#   # form = UserSignUpForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/signup.html', context)



