from django.contrib.auth.models import User
from django.test import TestCase, Client
from basket.models import notebook
from basket.models import Otlojit

class PostAdminTest(TestCase):
    # Тест на создание нового пользователя
    def ZakaZ(self):
        self.note = Otlojit.object.create(konkrnote = 3333,
                                          konkruser = 4444,
                                          zakax = 5555,
                                          user = 'testing',
                                          sostoyanie = 'Заказ обработан')
        self.assertEquals(str(self.note), 'testing')
