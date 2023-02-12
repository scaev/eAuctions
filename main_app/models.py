from django.db import models
from django.urls import reverse




class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.username

class Auction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'auction_id': self.id})

class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.amount} on {self.auction}"

<<<<<<< HEAD
class Photo(models.Model):
    url = models.CharField(max_length=200)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.auction_id} @{self.url}"
=======
>>>>>>> 4830b8905db52dcf1a32eaebf9e3eaa5cf1be66f
