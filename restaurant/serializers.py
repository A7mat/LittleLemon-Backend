from rest_framework import serializers
from .models import MenuItem, Booking, Category
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class MenuItemSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    category = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = MenuItem
        fields = '__all__'
        extra_kwargs = {
            'price': {'min_value': 0},
            'inventory': {'min_value': 0},
            'title': {
                'validators': [
                    UniqueValidator(
                        queryset=MenuItem.objects.all()
                    )
                ]
            }
            }

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        