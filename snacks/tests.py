from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class SnacksTests(SimpleTestCase):
    def test_home_exists(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_using_correct_templates(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
