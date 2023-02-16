from django.db import models
from django.urls import reverse
from datetime import date 
from django.contrib.auth.models import User

CONDITION_CHOICES = (('new','NEW'), ('used','USED'), ('refurbished','REFURBISHED'))
CATEGORY_CHOICES = (('antiques', 'ANTIQUES'),('art', 'ART'),('electronics','ELECTRONICS'),('furniture', 'FURNITURE'), ('jewelry', 'Jewelry'),('tools', 'TOOLS'), ('others', 'OTHERS') )



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    


    

class Auction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=11, choices=CATEGORY_CHOICES, default='others')
    condition = models.CharField(max_length=11, choices=CONDITION_CHOICES, default='used')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['end_date']
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'auction_id': self.id})
class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.amount} on {self.auction}"
    
    class Meta:
        ordering = ['-amount']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for auction_id: {self.auction_id} @{self.url}"

