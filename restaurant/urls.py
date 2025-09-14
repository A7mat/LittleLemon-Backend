from django.urls import path
from .views import MenuItemView, SingleMenuItemView #, BookingView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', views.index, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu'),
    # path('booking/', BookingView.as_view(), name='booking'),
    path('api-token-auth/', obtain_auth_token)
]