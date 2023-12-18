from django.test import TestCase
from django.urls import reverse_lazy
from coffe.views import MyLoginView

class MyLoginViewTest(TestCase):
    def test_get_success_url(self):
        view = MyLoginView()
        view.success_url = reverse_lazy('coffe:list_item')
        self.assertEquals(view.get_success_url(), reverse_lazy('coffe:list_item'))
    def test_template_used(self):
        response = self.client.get('/coffe/user/login/')
        self.assertTemplateUsed(response, 'coffe/login.html')

    def test_successful_login_redirect(self):
        login_url = reverse_lazy('coffe:login')
        response = self.client.post(login_url, {'username': 'test user', 'password': 'test password'})
        self.assertRedirects(response, '/coffe/item/list/')

    def test_failed_login_redirect(self):
        login_url = reverse_lazy('coffe:login')
        response = self.client.post(login_url, {'username': 'wrong username', 'password': 'wrong password'})
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/coffe/user/login/')
        self.assertContains(response, "Invalid username or password")
        # self.assertFormError(response, 'username', 'Invalid username or password')