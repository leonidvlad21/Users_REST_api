from django.db import models
from datetime import date

# Create your models here.

class Userset(models.Model):
  a_status = (
    ('A', 'Активен'),
    ('N', 'Неактивен'),
  )

  name = models.CharField("username", max_length=128)
  email = models.EmailField("email", max_length=64)
  password = models.CharField("password", max_length=128, default="none password")
  register_date = models.DateField("date", default=date.today)
  status = models.CharField(max_length=1, choices=a_status, blank=True,
                            default='A', help_text='Статус пользователя', )

  class Meta:
    ordering = ['name']
    get_latest_by = "id"  # debug

  def __str__(self):
    print('name: ', self.name)
    return self.name

