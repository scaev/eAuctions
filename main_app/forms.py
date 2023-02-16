from django.forms import ModelForm
from .models import Bid

class BiddingForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']





