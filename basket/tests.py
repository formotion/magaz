from django.contrib.auth.models import User
from django.test import TestCase, Client
from basket.models import notebook
from basket.models import Otlojit


class HomePageTest(TestCase):
    # Тест на добавление новой модели нотбука
    def setUp(self):
        self.note = notebook.objects.create(model='NewNotebook',
                                            cost=1,
                                            amount=2)
        self.assertEqual(str(self.note), 'NewNotebook')
