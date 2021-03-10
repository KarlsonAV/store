from django.urls import path

from .views import SearchView, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
]