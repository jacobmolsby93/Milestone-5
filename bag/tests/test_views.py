from django.test import TestCase, Client, RequestFactory
from decimal import Decimal

from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
from styles.models import ShopStyles

class TestBag(TestCase):

    def setUp(self):
        self.client = Client()
        self.view_bag_url = reverse('view_bag')
        self.request = RequestFactory().get('/')

        # adding session
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.existing_style = ShopStyles(
            style_name='test style',
            style_price='2.3',
            style_description='test decription'
        )

        self.new_style = ShopStyles(
            style_name='testname1',
            style_price=Decimal('3.4'),
            style_description='some description'
        )

        self.request.session['bag'] = {
            'item_id': 1,
            'quantity': 1,
            'style': self.existing_style
        }

    def test_cart_add_to_existing_quantity(self):
        """
        Test adding a quantity to an existing quantity.
        """
        request = self.request
        bag = request.session['bag']
        new_bag = {
            'item_id': 1,
            'quantity': 1,
            'style': self.existing_style
        }

        self.assertEquals(new_bag, bag)

    def test_view_bag(self):
        """
        Test the view bag view.
        """
        response = self.client.get(self.view_bag_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

        
            
        