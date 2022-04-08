from django.test import TestCase
from django.urls import reverse, resolve
from bag.views import (
    view_bag,
    add_to_bag,
    remove_from_bag
)


class TestUrls(TestCase):
    """
    A class for testing each of the urls in bag app
    """

    def test_view_bag_url(self):
        """
        A test for the view bag url.
        """
        url = reverse('view_bag')
        self.assertEquals(resolve(url).func, view_bag)

    def test_add_item_to_bag_url(self):
        """
        A test for the add item to bag url.
        """
        url = reverse('add_to_bag', args=['item_id'])
        self.assertEquals(resolve(url).func, add_to_bag)
    
    def test_delete_item_from_bag_url(self):
        """
        A test for the delete item from bag url.
        """
        url = reverse('remove_from_bag', args=['item_id'])
        self.assertEquals(resolve(url).func, remove_from_bag)