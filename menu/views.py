from django.template.loader import render_to_string
from django.http import HttpRequest, HttpResponse
from django.shortcuts import Http404
from menu.models import *
from django.conf import settings

# Create your views here.
def item(request, key):

	try:
		article = Item.objects.get(id=key).text
		if article=='':
			article = ' Упс, текст не найден... '
		return HttpResponse(render_to_string('main.html', locals()))
	except:
		raise Http404(' Объект не найден! Попробуйте другой ')

def main(request):
	return HttpResponse(render_to_string('main.html'))