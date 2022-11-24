from django.test import TestCase
from django.urls import reverse

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('core:home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class AboutTests(TestCase):
    def test_about_view_status_code(self):
        url = reverse('core:about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class FeedbackTests(TestCase):
    def test_feedback_view_status_code(self):
        url = reverse('core:feedback_create')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class FeedbackTests(TestCase):
     def test_feedback_view_status_code(self):
        url = reverse('core:feedback_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class BookServiceTests(TestCase):
    def test_about_view_status_code(self):
        url = reverse('core:book_service')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class AboutTests(TestCase):
    def test_about_view_status_code(self):
        url = reverse('core:about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class CheckoutTests(TestCase):
    def test_checkout_view_status_code(self):
        url = reverse('core:checkout')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class ServiceTests(TestCase):
    def test_service_view_status_code(self):
        url = reverse('core:delivery')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class ServiceTests(TestCase):
    def test_service_view_status_code(self):
        url = reverse('core:service_history')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class PaymentTests(TestCase):
    def test_payment_view_status_code(self):
        url = reverse('core:payment')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class PaymentCompletedTests(TestCase):
    def test_paymentcompleted_view_status_code(self):
        url = reverse('core:payment_completed')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class PaymentTests(TestCase):
    def test_payment_view_status_code(self):
        url = reverse('core:payment_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)