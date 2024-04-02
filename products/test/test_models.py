from django.test import TestCase
from model_bakery import baker
from products.models import Product




class testproductmodel(TestCase):
    def setUp(self):
        self.product=baker.make(Product, title='chocolate')
        
    def test_model_str(self):
        self.assertEqual(str(self.product),'chocolate')
