from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, decription="Very delicious")
        self.assertEqual(item, "IceCream: 80")