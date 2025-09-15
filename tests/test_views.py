from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    # def setUp(self):
    #     item = MenuItem.objects.create(title="shakshuka", price= 15.00, inventory=9)
    #     item = MenuItem.objects.create(title="Hummus", price= 4.00, inventory=4)

    # def test_get_all(self):
    #     response = self.client.get('/restaurant/menu-items/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'shakshuka')
    #     self.assertContains(response, 'Hummus')
        
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(title="Pizza", price=12, inventory=20)
        MenuItem.objects.create(title="Pasta", price=10, inventory=15)

    def test_getall(self):
        url = reverse('menu')   # name matches the DRF router for MenuViewSet
        response = self.client.get(url)
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
