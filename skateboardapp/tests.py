from rest_framework.test import APITestCase
from django.urls import reverse
from skateboardapp.models import Skateboard
from skateboardapp.serializers import SkateboardSerializer
from rest_framework import status

# Create your tests here.
class get_post_put_del_test(APITestCase):
    def setUp(self):
        self.home_url = reverse('skateboard')
        self.Skateboard_listing_1 = Skateboard.objects.create(
            available = 1,
            owner = "Will",
            brand = "Element",
            weight = "5",
            length = '30',
            type = "skateboard",
            city = "Buffalo",
            state = "NY"
        )

        self.Skateboard_listing_2 = Skateboard.objects.create(
            available = 0,
            owner = "Jun",
            brand = "Bird",
            weight = "6",
            length = '15',
            type = "pennyboard",
            city = "Detroit",
            state = "MI"
        )

    def test_get(self):
        url = self.home_url
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        data = {
            "available" : 0,
            "owner": "Kyle",
            "brand": "Element",
            "weight": 8,
            "length": 40,
            "type": "longboard",
            "city": "Cleveland",
            "state": "OH"
        }
        response = self.client.post(self.home_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Skateboard.objects.count(), 3)
        self.assertEqual(Skateboard.objects.get(owner="Kyle").id, 3)
        self.assertEqual(Skateboard.objects.get(owner="Kyle").owner, data['owner'])