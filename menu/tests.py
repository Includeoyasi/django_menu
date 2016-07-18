from django.test import TestCase, Client
from django.template import Template, Context
from django.core.urlresolvers import reverse
from menu.models import Item

# Create your tests here.
class TemplateTagTest(TestCase):

	def setUp(self):

		""" Формирует переменные для тестов	"""

		self.TEMPLATE_WITH_VOID_KEY = Template("{% load menu %}{% draw_menu %}")
		self.TEMPLATE = Template("{% load menu %}{% draw_menu 'main_menu' %}")
		self.client = Client()

	def test_void_key(self):

		"""	Проверяет рендер при полном отсутствии параметров для draw_menu """

		render = self.TEMPLATE_WITH_VOID_KEY.render(Context({}))
		self.assertEqual(render, '\n\n<ul class="nav">\n\n</ul>')

	def test_invalid_key(self):

		""" Проверяет обработку несущетсвующих пунктов меню """

		response = self.client.get('/0/')
		self.assertEqual(response.status_code, 404)

	def test_random_url(self):

		""" Проверяет обработку несуществующих страниц """

		response = self.client.get('/randomURL2016/')
		self.assertEqual(response.status_code, 404)

	def test_context_request_for_main_page(self):

		""" Проверяет наличие request в context для главной страницы """

		response = self.client.get('/')
		self.assertEqual('request' not in response.context, True)