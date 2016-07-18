from django.db import models

# Create your models here.
class Item(models.Model):
	class Meta:
		verbose_name = "Пункт меню"
		verbose_name_plural = "Пункты меню"
	father = models.ForeignKey("Item", blank=True, null=True)
	title = models.CharField(max_length=1024,null=True, blank=True, verbose_name='Оглавление')
	text = models.TextField(null=True, blank=True, verbose_name='Текст')

	def __str__(self):
		return self.title