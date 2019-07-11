from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
	def setUp(self):
		Post.objects.create(text = 'test text')

	def test_text_contents(self):
		post = Post.objects.get(id=1)
		expected_objects_name = f'{post.text}'
		self.assertEqual(expected_objects_name, 'test text')


class HomePageViewTest(TestCase):
	def setUp(self):
		Post.objects.create(text='another test')

	def test_view_url_exists_at_proper_locations(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_view_url_by_name(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'home.html')