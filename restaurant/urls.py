from django.urls import path
from .views import MenuItemView, SingleMenuItemView #, BookingView

urlpatterns = [
    # path('', views.index, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu'),
    # path('booking/', BookingView.as_view(), name='booking'),
]