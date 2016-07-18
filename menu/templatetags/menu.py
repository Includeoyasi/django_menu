from django import template
from menu.models import *

register = template.Library()

def get_params(all_items, key, father):

	""" Функция собирающая необходимые параметры для рендера пунктов меню """

	items = [item for item in all_items if item.father_id == father]
	if father not in items:
		for item in all_items:
			if item.id==int(key):
				father = item
				break
		while father not in items:
			father = get_father(all_items, father)
	return {'items': items, 'key': key, 'father': father, 'all_items': all_items}

def get_father(all_items, item):

	""" Функция получает на выход пункт меню и пытается получить его родителя """

	father = item.father_id
	for item in all_items:
		if item.id==father:
			father = item
			break
	return father

@register.filter(name='is_father')
def is_father(item_id, father):

	""" Функция для сравнения двух переменных """

	return True if item_id==father else False

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, key=None, all_items=None, father=None):

	""" Основная функция тега draw_menu формирует главное меню и его дерево
		Принимает следующие параметры:

		context - системный параметр, необходим для определения пункта меню,
		по которому было совершенно нажатие.

		key - переменная определяющая глубину вложенности

		all_items - переменная, для передачи QwerySet'a сквозь шаблон,
			во время рекурсивного рендера меню

		father - переменная определяющая текущую ступеньку вложенности меню

	"""
	if not all_items:
		all_items = Item.objects.all()

	if 'request' in context: # Запрос на один из пунктов меню
		key = context['request'].path.split('/')[1]
		return get_params(all_items, key, father)
	else: # Запрос на начальную страницу или рекусивный вызов функции из шаблона
		if key == 'main_menu' or key==None or str(father)==key:
			items = [item for item in all_items if item.father_id == father]
			return {'items': items, 'key': None, 'father': None}
		else:
			return get_params(all_items, key, father)