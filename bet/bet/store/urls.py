from django.urls import path
from . import views
from store.controller import authview


urlpatterns = [
    path('', views.home, name="home"),
    path('sure_bets/', views.sure_bets, name="sure_bets"),
    path('prediction_history/', views.prediction_history, name="prediction_history"),
    path('Odds/', views.Odds, name="Odds"),
    path('vip_odds/', views.vip_odds, name="vip_odds"),
    path('payment/', views.modal, name="modal"),
    path('register/', authview.register, name="register" ),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),



]