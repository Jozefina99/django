from django.urls import path
from ticketSales import views

urlpatterns = [
    path('concert/list', views.concertListView),
    path('location/list', views.locationListView),
    path('concert/<int:concert_id>', views.concertDetailesView),
    path('time/list', views.timeView)
]
