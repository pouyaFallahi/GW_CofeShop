from django.test import SimpleTestCase
from django.urls import reverse, resolve
from coffe.views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView, CustomerSignupView, MyLoginView


# create_item
# update_item
# delete_item
# signup_user
# login
class TestUrls(SimpleTestCase):

    def test_ItemList_url_is_resolved(self):
        url = reverse('coffe:list_item')
        self.assertEquals(resolve(url).func.view_class, ItemListView)

    def test_item_create_url_is_resolved(self):
        url = reverse('coffe:create_item')
        self.assertEquals(resolve(url).func.view_class, ItemCreateView)

    def test_item_update_url_is_resolved(self):
        url = reverse('coffe:update_item', args=['1'])
        self.assertEquals(resolve(url).func.view_class, ItemUpdateView)

    def test_item_delete_url_resolved(self):
        url = reverse('coffe:delete_item', args=['1'])
        self.assertEquals(resolve(url).func.view_class, ItemDeleteView)

    def test_signup_url_resolved(self):
        url = reverse('coffe:signup_user')
        self.assertEquals(resolve(url).func.view_class, CustomerSignupView)

    def test_login_url_resolved(self):
        url = reverse('coffe:login')
        self.assertEquals(resolve(url).func.view_class, MyLoginView)
