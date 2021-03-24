from django.urls import path

from .views import HomePageView, AboutPageView, TeamPageView
# from .views import TradeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('team/', TeamPageView.as_view(), name='team'),
]
