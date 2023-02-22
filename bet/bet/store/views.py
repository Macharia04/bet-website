from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users 









# Create your views here.

def home(request):
    return render(request, "store/index.html")


@allowed_users(allowed_roles=['Admin', 'Vip'])
def sure_bets(request):
    return render(request, "store/odds/sure_bets.html")


def prediction_history(request):
    return render(request, "store/odds/prediction_history.html")

def modal(request):
    return render(request, "store/payment/modal.html")
   
def Odds(request):
    return render(request, "store/odds/Odds.html")


@allowed_users(allowed_roles=['Vip'])
def vip_odds(request):
    return render(request, "store/odds/vip_odds.html")


