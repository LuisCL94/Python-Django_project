from django.core import mail
from django.test import TestCase, Client
from django.core.urlresolvers import reverse 
# Create your tests here.
class UriViewTest(TestCase):

	def test_uri_status_end_templates(self):
		client = Client()
		response = client.get(reverse('blog:uri'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/uri_list.html')
		