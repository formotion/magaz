﻿from django.contrib.auth.models import User
from django.test import TestCase, Client
from basket.models import notebook


class HomePageTest(TestCase):
	# Тест на проверку работоспособности домашней страницы    
	def test_homepage_available(self):       
		c = Client()       
		response = c.get('/')     
		self.assertEquals(response.status_code, 200)

	# Тест на добавление новой модели нотбука   
	def setUp(self):
		self.note = notebook.objects.create(model='NewNotebook',                  
							cost=1,
              						amount=2)
		self.assertEqual(str(self.note), 'NewNotebook')

class PostAdminTest(TestCase):
	# Тест на авторизацию НЕ admin'а в админке
	def test_na_vhod_NE_admina(self):
		c = Client()
		c.login(username='test', password='test')
		response = c.get('/admin/')
		self.assertEquals(response.status_code, 302)