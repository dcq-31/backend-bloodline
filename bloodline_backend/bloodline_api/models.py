from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# User Model
class User(AbstractUser):
  created_at = models.DateTimeField('created date', auto_now_add=True)
  update_at = models.DateTimeField('last update', auto_now=True)
  
  def __str__(self):
    return self.get_full_name()
  
"""
Add Fields
image
"""
# Dog Model
class Dog(models.Model):
  # Choises of breed (for example)
  AFGHAN_HOUND = 'AF'
  PEKINGESE = 'PE'
  BASSADOR = 'BA'
  DOGS_BREED_CHOICHES = (
    (AFGHAN_HOUND, 'Afghan Hound'),
    (PEKINGESE, 'Pekingese'),
    (BASSADOR, 'Bassador'),
  )
  name = models.CharField(max_length=100)
  code = models.CharField('identification code', max_length=10, unique=True)
  owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='dogs', verbose_name='related user', default=1)
  date_birth = models.DateTimeField('date of birthday')
  breed = models.CharField('animal species', choices=DOGS_BREED_CHOICHES, max_length=2)
  partners = models.ManyToManyField('self', blank=True, verbose_name='related partners')
  litters = models.ManyToManyField('self', blank=True, verbose_name='related litters')
  siblings = models.ManyToManyField('self', blank=True, verbose_name='related siblings')
  created_at = models.DateTimeField('created date', auto_now_add=True)
  update_at = models.DateTimeField('last update', auto_now=True)
  
  def __str__(self):
    return self.name + " | " + self.code